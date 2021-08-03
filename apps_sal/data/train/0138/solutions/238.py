

# dp[i][0] : max length of subarray ending with index i With positive product
# dp[i][1] : max length of subarray ending with index i With negative product


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))]
        res = 0
        if nums[0] > 0:
            dp[0][0] = 1
        elif nums[0] < 0:
            dp[0][1] = 1
        # print(dp)
        res = max(res, dp[0][0])
        for idx in range(1, len(nums)):
            if nums[idx] == 0:
                dp[idx][0], dp[idx][1] = 0, 0
            elif nums[idx] > 0:
                dp[idx][0] = dp[idx - 1][0] + 1
                if dp[idx - 1][1] > 0:
                    dp[idx][1] = dp[idx - 1][1] + 1
                res = max(dp[idx][0], res)

            elif nums[idx] < 0:
                dp[idx][1] = dp[idx - 1][0] + 1
                if dp[idx - 1][1] > 0:
                    dp[idx][0] = dp[idx - 1][1] + 1
                res = max(res, dp[idx][0])

        # print(dp)
        return res


'''
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        diction = {}
        diction[\"pos\"], diction[\"neg\"] = 0, 0
        prevpos, prevneg = 0, 0
        res = 0
        for num in nums:
            if num == 0:
                diction[\"pos\"], diction[\"neg\"] = 0, 0
                prevpos, prevneg = 0, 0
            elif num > 0:
                diction[\"pos\"] += 1
                if diction[\"neg\"] % 2 == 0:
                    res = max(res, diction[\"pos\"]+diction[\"neg\"]+prevpos)
                    print(num, res)
                else:
                    res = max(res, diction[\"pos\"], prevpos)
        
            elif num < 0:
                diction[\"neg\"] += 1
                print(\"neg\", num, diction[\"neg\"], diction[\"pos\"], prevpos)
                if diction[\"neg\"] % 2 == 1:
                    res = max(res, diction[\"pos\"])
                    prevpos += diction[\"pos\"]
                    diction[\"pos\"] = 0
                else:
                    res = max(res, diction[\"pos\"]+diction[\"neg\"]+prevpos)
                    prevpos = diction[\"neg\"] + diction[\"pos\"] + prevpos
                    diction[\"neg\"] = 0
                    diction[\"pos\"] = 0
                    
        print(res)
        return res
'''


'''
        diction = {}
        diction[\"pos\"], diction[\"neg\"] = 0, 0
        res = 0
        for num in nums:
            if num == 0:
                diction[\"pos\"], diction[\"neg\"] = 0, 0
            elif num > 0:
                diction[\"pos\"] += 1
                if diction[\"neg\"] % 2 == 0:
                    res = max(res, diction[\"pos\"]+diction[\"neg\"])
            elif num < 0:
                diction[\"neg\"] += 1
                
                if diction[\"neg\"] % 2 == 1:
                    res = max(res, diction[\"pos\"]+diction[\"neg\"]-1)
                else:
                    res = max(res, diction[\"pos\"]+diction[\"neg\"])
                
        print(res)
        
        return res
        

'''
