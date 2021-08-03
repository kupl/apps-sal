from collections import defaultdict


class Solution:
    def largestComponentSize(self, a: List[int]) -> int:
        d = {}

        def find(x):
            if x != d.setdefault(x, x):
                d[x] = find(d[x])
            return d[x]

        def union(x, y):
            d[find(x)] = find(y)

        for n in a:
            for i in range(2, int(n**0.5) + 1):
                if n % i:
                    continue
                union(n, i)
                union(n, n // i)

        counter = Counter(find(i) for i in a)
        return max(counter.values())
