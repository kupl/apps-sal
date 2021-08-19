class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        '''        
        # top-down TLE
        dp = [0] + [float('inf')]*n
        def helper(k):
            if not (1<= k <= n):
                return 0
            if dp[k]!=float('inf'):
                return dp[k]
            dp[k] = min([helper(i-x)+1 for i, x in enumerate(ranges)\\
                      if k in range(i-x+1, i+x+1)] or [-1])
            return dp[k]
        return helper(n)
        '''

        if n == 0:
            return 0
        dp = [0] + [float('inf')] * n
        for i, x in enumerate(ranges):
            start, end = max(0, i - x), min(n, i + x)
            for j in range(start, end + 1):
                dp[j] = min(dp[j], dp[start] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1

        '''        
        # greedy
        covers = sorted([[i-x, i+x] for i, x in enumerate(ranges)], key = lambda x: (x[0], -x[1]))
        #print(covers)
        res, prev_end, end = 0, -float('inf'), 0
        for src, dest in covers:
            if src > end or end >= n:
                break
            if prev_end < src <= end:
                prev_end, res = end, res + 1
            end = max(end, dest)
        return res if end >= n else -1
        '''
