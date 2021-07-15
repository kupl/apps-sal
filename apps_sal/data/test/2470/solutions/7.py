class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        from bisect import bisect_right as br
        arr2.sort()
        
        dp = {0:-math.inf}
        min_cnt = 0
        for n1 in arr1:
            # print(n1)
            new_dp = {}
            cnt = min_cnt
            while cnt in dp:
                if n1 > dp[cnt]:
                    new_dp[cnt] = min(new_dp.get(cnt, math.inf), n1)
                    # candidate = min(new_dp.get(cnt, math.inf), n1)
                    # if candidate < new_dp.get(cnt-1, math.inf):
                    #     new_dp[cnt] = candidate
                i2 = br(arr2, dp[cnt])
                # if i2 < len(arr2) and arr2[i2] < new_dp.get(cnt, math.inf):
                if i2 < len(arr2):
                    new_dp[cnt+1] = arr2[i2]
                # print(new_dp)
                # if new_dp.get(cnt+1, -math.inf) >= new_dp.get(cnt, math.inf):
                #     new_dp.pop(cnt+1)
                # if new_dp.get(cnt, -math.inf) >= new_dp.get(cnt-1, math.inf):
                #     new_dp.pop(cnt)
                cnt += 1
            if len(new_dp) == 0:
                return -1
            while min_cnt not in new_dp:
                min_cnt += 1
            dp = new_dp
            print(dp)
        return min(dp.keys())

