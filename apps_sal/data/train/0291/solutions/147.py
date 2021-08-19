class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        dp = [[0, 0]]
        ans = 0
        for i in arr:
            if i % 2 == 0:
                dp.append([dp[-1][0] + 1, dp[-1][1]])
            else:
                dp.append([dp[-1][1], dp[-1][0] + 1])
            ans += dp[-1][1]
        return int(ans % (1000000000.0 + 7))
