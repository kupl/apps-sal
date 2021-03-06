class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        set_a = set(A)
        MAX_NUMBER = max(A)
        SQRT_MAX_NUMBER = int(math.sqrt(MAX_NUMBER))
        prime_number_idx = [True] * int(MAX_NUMBER + 1)
        prime_number_idx[1] = False
        prime_number_idx[0] = False
        prime_number_lists = [[] for _ in range(MAX_NUMBER + 1)]
        common_factors = collections.defaultdict(list)
        for i in range(2, len(prime_number_idx)):
            if not prime_number_idx[i]:
                continue
            num = i
            while num <= MAX_NUMBER:
                if num in set_a:
                    common_factors[i].append(num)
                prime_number_lists[num].append(i)
                prime_number_idx[num] = False
                num += i
        visited = set()

        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            num = 1
            while prime_number_lists[node]:
                factor = prime_number_lists[node].pop()
                while common_factors[factor]:
                    neighbor = common_factors[factor].pop()
                    num += dfs(neighbor)
            return num
        return max([dfs(node) for node in A])
