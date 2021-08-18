class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        dp = [(0, 0)]
        if nums[0] < 0:
            dp[0] = (0, 1)
        elif nums[0] > 0:
            dp[0] = (1, 0)
        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp.append((0, 0))
            elif nums[i] > 0:
                if nums[i - 1] != 0:
                    if dp[i - 1][1] != 0:
                        dp.append((dp[i - 1][0] + 1, dp[i - 1][1] + 1))
                    else:
                        dp.append((dp[i - 1][0] + 1, 0))
                else:
                    dp.append((1, 0))
            elif nums[i] < 0:
                if nums[i - 1] != 0:
                    if dp[i - 1][1] != 0:
                        dp.append((dp[i - 1][1] + 1, dp[i - 1][0] + 1))
                    else:
                        dp.append((0, dp[i - 1][0] + 1))
                else:
                    dp.append((0, 1))
        positives = [dp[i][0] for i in range(len(nums))]
        return max(positives)

        maxProd = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                maxProd = 1
        prods = [nums[0]]
        zeroFound = [False] * len(nums)
        if nums[0] == 0:
            zeroFound[0] = True
        for i in range(1, len(nums)):
            if zeroFound[i - 1] or nums[i] == 0:
                zeroFound[i] = True
        mostRecentPostZeroNeg = [float('-inf')] * len(nums)
        if nums[0] < 0:
            mostRecentPostZeroNeg[0] = 0
        for i in range(1, len(nums)):
            if nums[i] == 0:
                continue
            if nums[i] > 0:
                mostRecentPostZeroNeg[i] = mostRecentPostZeroNeg[i - 1]
            if nums[i] < 0:
                if mostRecentPostZeroNeg[i - 1] == float('-inf'):
                    mostRecentPostZeroNeg[i] = i
                else:
                    mostRecentPostZeroNeg[i] = mostRecentPostZeroNeg[i - 1]
        for i in range(1, len(nums)):
            if prods[i - 1] == 0:
                if nums[i] > 0:
                    prods.append(1)
                elif nums[i] < 0:
                    prods.append(-1)
                else:
                    prods.append(0)
            elif prods[i - 1] < 0:
                if nums[i] < 0:
                    prods.append(1)
                elif nums[i] > 0:
                    prods.append(-1)
                else:
                    prods.append(0)
            elif prods[i - 1] > 0:
                if nums[i] < 0:
                    prods.append(-1)
                elif nums[i] > 0:
                    prods.append(1)
                else:
                    prods.append(0)

        dp = []
        if nums[0] == 0:
            dp.append(0)
        if nums[0] < 0:
            dp.append(1)
        if nums[0] > 0:
            dp.append(1)
        dp1 = []
        if nums[0] < 0:
            dp1.append(0)
        if nums[0] > 0:
            dp1.append(0)
        if nums[0] == 0:
            dp1.append(0)
        for i in range(1, len(nums)):
            if dp1[-1] == 0:
                if nums[i] < 0:
                    dp1.append(1)
                else:
                    dp1.append(0)
            else:
                if nums[i] == 0:
                    dp1.append(0)
                else:
                    dp1.append(dp1[-1] + 1)

        for i in range(1, len(nums)):
            if nums[i] != 0:
                dp.append(dp[i - 1] + 1)
            else:
                dp.append(0)
            if prods[i] > 0:
                maxProd = max(maxProd, dp[i])
            else:
                if mostRecentPostZeroNeg[i] != float('-inf'):
                    maxProd = max(maxProd, i - mostRecentPostZeroNeg[i])
        return maxProd

        '''if all(i == 0 for i in nums):
            return 0
        if len(nums) == 1:
            if nums[0] < 0:
                return 0
        dp = []
        if nums[0] == 0:
            dp.append((0,0))
        elif nums[0] > 0:
            dp.append((1,0))
        elif nums[0] < 0:
            dp.append((0,1))
        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp.append((0,0))
            elif nums[i] > 0:
                dp.append((dp[i-1][0]+1, dp[i-1][1]))
            else:
                dp.append((dp[i-1][0], dp[i-1][1]+1))
        print(dp)
        maxV = 0
        for i in range(len(dp)):
            if dp[i][1] % 2 == 0:
                maxV = max(maxV, dp[i][0] + dp[i][1])
        return maxV'''

        '''dp = []
        if nums[0] <= 0:
            dp.append(0)
        else:
            dp.append(1)
        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp.append(0)
            elif nums[i] < 0:
                if dp[i-1] == 0:
                    dp.append(0)
                elif nums[i-1] < 0:
                    dp.append()
                else:
                    dp.append(dp[-1]+1)
            else: 
                if dp[i-1] == 0:
                    if nums[i-1] == 0:
                        dp.append(1)
                    else:
                        dp.append(1)
                elif nums[i-1] < 0:
                    dp.append(dp[i-1] + 1)
                else: 
                    dp.append(dp[i-1] + 1)
            
            
        return dp[len(nums)-1]'''
