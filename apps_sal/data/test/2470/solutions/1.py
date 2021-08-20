class Solution:

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        from bisect import bisect_right as br
        arr2.sort()
        dp = {0: -math.inf}
        for n1 in arr1:
            new_dp = {}
            for cnt in dp:
                if n1 > dp[cnt]:
                    new_dp[cnt] = min(new_dp.get(cnt, math.inf), n1)
                i2 = br(arr2, dp[cnt])
                if i2 < len(arr2):
                    new_dp[cnt + 1] = min(new_dp.get(cnt + 1, math.inf), arr2[i2])
                cnt += 1
            if len(new_dp) == 0:
                return -1
            dp = new_dp
        return min(dp.keys())
