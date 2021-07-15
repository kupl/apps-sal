class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        if n < 1 or ranges is None: return -1
        dp = [None]*len(ranges)
        # for each tap
        for i in range(len(dp)):
            # calc tap left and right extent
            l = max(0, i-ranges[i])
            r = min(len(dp)-1, i+ranges[i])
            # for each cell in extent, take the min of the cell or the left extent of the tap
            for j in range(l, r+1):
                if dp[j] is None:
                    dp[j] = l
                else:
                    dp[j] = min(dp[j], l)
            # since we can reach to front from last, only one tap is required
            if dp[-1] == 0:
                return 1
        # start from end, jump backwards incrementing tap count each time
        # careful to exit if no jump can be made
        i = len(dp)-1
        c = 0
        while i > 0 and dp[i] is not None and dp[i] != i:
            i = dp[i]
            c += 1
        # if we can jump all the way to the front, then return the count else -1
        return c if i == 0 else -1
