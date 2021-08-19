class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        mp = {}
        ans = 0

        def find(a):
            if a not in mp:
                mp[a] = a
            if mp[a] != a:
                mp[a] = find(mp[a])
            return mp[a]

        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                mp[pa] = pb
        for a in A:
            t = int(math.sqrt(a))
            for k in range(2, t + 1):
                if a % k == 0:
                    union(a, k)
                    union(a, a / k)
        return max(collections.Counter([find(a) for a in A]).values())
