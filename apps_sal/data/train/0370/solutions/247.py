class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        from math import sqrt
        from collections import defaultdict
        initial = set(A)
        parent = defaultdict(int)

        for e in A:
            parent[e] = e

        def find(c):
            if c not in parent:
                parent[c] = c
                return c
            while parent[c] != c:
                parent[c] = parent[parent[c]]
                c = parent[c]
            return c

        def union(c1, c2):
            p1, p2 = find(c1), find(c2)
            if p1 == p2:
                return
            parent[p1] = p2

        for e in A:
            for n in range(2, int(sqrt(e)) + 1):
                if e % n == 0:
                    # divisible by n
                    union(e, e // n)
                    union(e, n)

        # print(parent)

        counts = defaultdict(int)
        for k in list(parent.keys()):
            if k in initial:
                counts[find(k)] += 1

        return max(counts.values())
