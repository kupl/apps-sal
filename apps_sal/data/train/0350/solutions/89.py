class Solution:
    def subarraysWithKDistinct(self, A, K):
        def atMostK(A, K):
            count = collections.Counter()
            res, l, window_count = 0, 0, 0
            for r, c in enumerate(A):
                if count[c] == 0:
                    window_count += 1
                count[c] += 1
                while window_count > K:
                    count[A[l]] -= 1
                    if count[A[l]] == 0:
                        window_count -= 1
                    l += 1
                res += r - l + 1
            return res
        return atMostK(A, K) - atMostK(A, K - 1)
