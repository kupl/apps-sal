class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def find(n):
            if n not in root:
                return n
            root[n] = find(root[n])
            return root[n]

        def union(n1, n2):
            (root1, root2) = (find(n1), find(n2))
            if root1 == root2:
                return
            (rank1, rank2) = (rank[root1], rank[root2])
            if rank1 > rank2:
                root[root2] = root1
                size[root1] += size[root2]
            elif rank1 < rank2:
                root[root1] = root2
                size[root2] += size[root1]
            else:
                root[root1] = root2
                size[root2] += size[root1]
                rank[root2] += 1

        def find_prime_factors(n):
            factors = set()
            while n % 2 == 0:
                factors.add(2)
                n //= 2
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    factors.add(i)
                    n //= i
            if n > 2:
                factors.add(n)
            return factors
        factor_to_num = collections.defaultdict(list)
        for n in A:
            for factor in find_prime_factors(n):
                factor_to_num[factor].append(n)
        root = {}
        rank = {n: 1 for n in A}
        size = {n: 1 for n in A}
        for factor in factor_to_num:
            first_root = find(factor_to_num[factor][0])
            for i in range(1, len(factor_to_num[factor])):
                union(first_root, factor_to_num[factor][i])
        return max(size.values())
