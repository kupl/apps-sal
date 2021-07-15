class Solution:
    # O(n x sqrt(max)) time, O(n x sqrt(max)) space
    def largestComponentSize(self, A: List[int]) -> int:
        
        # Somehow using this version will mysteriously have TLE
        def find_prime_factors(num):
            result = []
            candidate = 2
            cur_num = num
            upper_limit = int(math.sqrt(num))
            while candidate <= upper_limit:
                if cur_num % candidate == 0:
                    result.append(candidate)
                    while cur_num % candidate == 0:
                        cur_num //= candidate
                candidate += 1

            if cur_num != 1:
                result.append(cur_num)
            return result
        
        # Using the recursive version to avoid TLE, although it should have the same
        # time complexity as the iterative version
        # def find_prime_factors(num):
        #     for i in range(2, int(math.sqrt(num)) + 1):
        #         if num % i == 0:
        #             return find_prime_factors(num // i) | set([i])
        #     return set([num])
        
        def find_root(x):
            if root[x] != x:
                root[x] = find_root(root[x])
            return root[x]
        
        def union(x, y):
            root[find_root(x)] = root[find_root(y)]
        
        root = [i for i in range(len(A))]
        prime_factor_to_index = defaultdict(list)
        # O(n x sqrt(max))
        for i, num in enumerate(A):
            prime_factors = find_prime_factors(num)
            for factor in prime_factors:
                prime_factor_to_index[factor].append(i)
        
        # O(n x sqrt(max))
        for indices in list(prime_factor_to_index.values()):
            for i in range(1, len(indices)):
                union(indices[i - 1], indices[i])
        
        # O(n)
        root_count = Counter(find_root(i) for i in range(len(A)))
        return max(root_count.values())
        


