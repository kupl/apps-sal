class Solution:
    
    def minTaps1(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i in range(n+1):
            if ranges[i]:
                left = max(0, i - ranges[i])
                right = min(n, i + ranges[i])
                intervals.append((left, right))
        intervals.sort()
        res = 0
        max_pos = 0
        prev_max_pos = -1
        for i, j in intervals:
            # max_pos >= n: all range covered
            if max_pos >= n:
                break
            # i > max_pos: [max_pos, i] not covered
            if i > max_pos:
                return -1
            elif prev_max_pos < i <= max_pos: # (i, j) will cover new interval
                res = res + 1
                prev_max_pos = max_pos
                print((i, j), res)
            max_pos = max(max_pos, j)
        return res if max_pos >= n else -1
        
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0] + [n + 1] * n
        for i, x in enumerate(ranges):
            for j in range(max(i - x + 1, 0), min(i + x, n) + 1):
                dp[j] = min(dp[j], dp[max(0, i - x)] + 1)
        # print(dp)
        return dp[n] if dp[n] < n + 1 else -1
