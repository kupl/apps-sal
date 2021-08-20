class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        parent = {}

        def ufind(a):
            if a not in parent:
                parent[a] = a
            if a != parent[a]:
                parent[a] = ufind(parent[a])
            return parent[a]

        def uunion(a, b):
            ua = ufind(a)
            ub = ufind(b)
            parent[ua] = ub
        count = collections.Counter()
        for x in A:
            factors = []
            y = 2
            while x >= y * y:
                if x % y == 0:
                    factors.append(y)
                    while x % y == 0:
                        x //= y
                y += 1
            if x > 1:
                factors.append(x)
            for (a, b) in zip(factors, factors[1:]):
                uunion(a, b)
            if len(factors) > 0:
                count[factors[0]] += 1
        final_count = collections.Counter()
        for key in count.keys():
            final_count[ufind(key)] += count[key]
        best = 0
        for key in final_count.keys():
            best = max(best, final_count[key])
        return best
