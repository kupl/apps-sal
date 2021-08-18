class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        graphs = {}

        def prime_factors(n):
            factors = set()
            while n % 2 == 0:
                factors.add(2)
                n = n // 2

            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    factors.add(i)
                    n = n // i

            if n > 2:
                factors.add(n)
            return factors

        for num in A:
            facts = prime_factors(num)

            if num not in graphs:
                graphs[num] = set()
            for fact in facts:
                if fact not in graphs:
                    graphs[fact] = set()
                graphs[fact].add(num)
                graphs[num].add(fact)

        groups, n_group = {}, 0

        def dfs(factor, group_id):
            groups[factor] = group_id
            for next_factor in graphs[factor]:
                if next_factor not in groups:
                    dfs(next_factor, group_id)

        for f in graphs:
            if f not in groups:
                n_group += 1
                dfs(f, n_group)

        group_count = {}
        for num in A:
            group_id = groups[num]
            if group_id not in group_count:
                group_count[group_id] = 0
            group_count[group_id] += 1

        return max(group_count.values())
