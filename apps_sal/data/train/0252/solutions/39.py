

class Solution:
    def minTaps(self, n, A):
        dp = [0] + [n + 2] * n
        for i, x in enumerate(A):
            for j in range(max(i - x + 1, 0), min(i + x, n) + 1):
                dp[j] = min(dp[j], dp[max(0, i - x)] + 1)
        return dp[n] if dp[n] < n + 2 else -1


# class Solution:
#     def minTaps(self, n: int, ranges: List[int]) -> int:

#         covers = sorted([(i - ranges[i], i + ranges[i], i) for i in range(n + 1) if ranges[i]], key=lambda x: (x[0], -x[1]))
#         print(covers)
#         cnt = 0
#         most_right = float('-inf')
#         lst = []
#         for curr_left, curr_right, curr_idx in covers:
#             if curr_right > most_right:
#                 most_right = curr_right
#                 cnt += 1
#                 lst.append(curr_idx)
#         print(cnt)
#         return cnt if most_right >= n else -1
