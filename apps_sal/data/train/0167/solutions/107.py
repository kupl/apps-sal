class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        cache = {}
        return self.drop_iter(K, N, cache)

    def drop_iter(self, K, N, cache):
        if K == 1:
            return N
        if N == 0:
            return 0
        if (K, N) in cache:
            return cache[(K, N)]
        res = float('inf')
        # for i in range(1, N+1):
        #     temp = max(self.drop_iter(K, N-i, cache), self.drop_iter(K-1, i-1, cache)) + 1
        #     res = min(res, temp)
        left = 1
        right = N
        # self.drop_iter(K, N-i, cache) 单调减
        # self.drop_iter(K-1, i-1, cache) 单调增
        while left <= right:
            mid = (left + right) // 2
            borke = self.drop_iter(K - 1, mid - 1, cache)
            not_broke = self.drop_iter(K, N - mid, cache)
            if borke > not_broke:
                right = mid - 1
                res = min(borke + 1, res)
            else:
                left = mid + 1
                res = min(not_broke + 1, res)

        cache[(K, N)] = res
        return res
