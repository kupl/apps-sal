class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
#         max_range = [0] * (n + 1)
#         for idx, r in enumerate(ranges):
#             left, right = max(0, idx - r), min(n, idx + r)
#             max_range[left] = max(max_range[left], right - left)
        
#         # it's a jump game now
#         start, end, step = 0, 0, 0
#         while end < n:
#             step += 1
#             start, end = end, max(i + max_range[i] for i in range(start, end + 1))
#             if start == end:
#                 return -1
#         return step
        

        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for idx, r in enumerate(ranges):
            for j in range(max(idx - r + 1, 0), min(idx + r, n) + 1):
                dp[j] = min(dp[j], dp[max(0, idx - r)] + 1)
        return dp[n] if dp[n] < float('inf') else -1
        # dp = [0] + [float('inf')] * n
        # for idx, r in enumerate(ranges):
        #     for j in range(max(idx - r + 1, 0), min(idx + r, n) + 1):
        #         dp[j] = min(dp[j], dp[max(0, idx - r)] + 1)
        # return dp[n] if dp[n] < float('inf') else -1

