class Solution:
    def maxDistance(self, position, m):
        position.sort()
        N = len(position)
        l = math.inf
        for i in range(1, N):
            l = min(l, position[i] - position[i - 1])
        r = position[-1] - position[0] + 1

        def check(k):
            last = position[0]
            res = 0
            for i in range(1, N):
                if position[i] - last >= k:
                    res += 1
                    last = position[i]
            return res

        while l < r:
            k = (l + r) // 2
            if check(k) < m - 1:
                r = k
            else:
                l = k + 1
        return r - 1
