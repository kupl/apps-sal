class Solution:

    def superEggDrop(self, K: int, N: int) -> int:

        def dfs(e, f):
            if e == 1:
                return f
            if f == 0 or f == 1:
                return f
            if (e, f) in cache:
                return cache[e, f]
            (left, right) = (1, f + 1)
            while left < right:
                mid = left + (right - left) // 2
                (i, j) = (dfs(e - 1, mid - 1), dfs(e, f - mid))
                if i < j:
                    left = mid + 1
                else:
                    right = mid
            cache[e, f] = 1 + max(dfs(e - 1, left - 1), dfs(e, f - left))
            return cache[e, f]
        cache = dict()
        return dfs(K, N)
