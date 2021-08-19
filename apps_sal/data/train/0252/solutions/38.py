class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        taps = []
        for i in range(len(ranges)):
            taps.append((i - ranges[i], i + ranges[i]))
        taps.sort()

        @lru_cache(None)
        def helper(i):
            if i >= n + 1:
                return float('inf')
            if taps[i][1] >= n:
                return 1
            ans = float('inf')
            for j in range(i + 1, n + 1):
                if taps[j][0] > taps[i][1]:
                    break
                if taps[j][0] <= taps[i][1] and taps[j][1] > taps[i][1]:
                    ans = min(ans, 1 + helper(j))
            return ans
        ans = float('inf')
        for i in range(n, -1, -1):
            res = helper(i)
            if taps[i][0] <= 0 and res < ans:
                ans = res
        return -1 if ans == float('inf') else ans
