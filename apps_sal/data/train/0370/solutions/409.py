class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        parent = {}

        def find(a):
            if a not in parent:
                parent[a] = a
            if a != parent[a]:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a, b):
            ua = find(a)
            ub = find(b)
            parent[ua] = ub
        count = collections.Counter()
        for num in A:
            y = 2
            factors = []
            while num >= y * y:
                if num % y == 0:
                    factors.append(y)
                    while num % y == 0:
                        num = num // y
                y += 1
            if num > 1:
                factors.append(num)
            for (a, b) in zip(factors, factors[1:]):
                union(a, b)
            if len(factors) > 0:
                count[factors[0]] += 1
        count2 = collections.Counter()
        for key in list(count.keys()):
            count2[find(key)] += count[key]
        ans = 0
        for key in list(count2.keys()):
            ans = max(ans, count2[key])
        return ans
