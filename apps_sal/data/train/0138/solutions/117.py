class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        # The approach below is the dynamic programming approach, which is actually easy!
        # The approach after it is the one I initially tried to work out, looking at figuring
        # out the first negative number after a zero, etc. Too complicated!
        
        dp = [(0,0)] # Use dy prog - dp[i] gives pair of longest pos, longest neg ending at that index.
        if nums[0] < 0:
            dp[0] = (0, 1)
        elif nums[0] > 0:
            dp[0] = (1, 0)
        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp.append((0,0))
            elif nums[i] > 0:
                if nums[i-1] != 0:
                    if dp[i-1][1] != 0:
                        dp.append((dp[i-1][0]+1, dp[i-1][1]+1))
                    else:
                        dp.append((dp[i-1][0]+1, 0))
                else:
                    dp.append((1, 0)) 
            elif nums[i] < 0:
                if nums[i-1] != 0:
                    if dp[i-1][1] != 0:
                        dp.append((dp[i-1][1] + 1, dp[i-1][0] + 1))
                    else:
                        dp.append((0, dp[i-1][0] + 1))
                else:
                    dp.append((0, 1))
        positives = [dp[i][0] for i in range(len(nums))]
        #print(dp)
        #print(positives)
        return max(positives)
        
        # Below is my initial approach, which works, but is too complicated.
        
        maxProd = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                maxProd = 1
        prods = [nums[0]]
        zeroFound = [False] * len(nums)
        if nums[0] == 0:
            zeroFound[0] = True
        for i in range(1, len(nums)):
            if zeroFound[i-1] or nums[i] == 0:
                zeroFound[i] = True
        mostRecentPostZeroNeg = [float('-inf')]* len(nums)
        if nums[0] < 0:
            mostRecentPostZeroNeg[0] = 0
        for i in range(1, len(nums)):
            if nums[i] == 0:
                continue
            if nums[i] > 0:
                mostRecentPostZeroNeg[i] = mostRecentPostZeroNeg[i-1]
            if nums[i] < 0:
                if mostRecentPostZeroNeg[i-1] == float('-inf'): #and zeroFound[i-1] == True:
                    mostRecentPostZeroNeg[i] = i
                else:
                    mostRecentPostZeroNeg[i] = mostRecentPostZeroNeg[i-1]
        for i in range(1, len(nums)):
            if prods[i-1] == 0:
                if nums[i] > 0:
                    prods.append(1)
                elif nums[i] < 0:
                    prods.append(-1)
                else:
                    prods.append(0)
            elif prods[i-1] < 0:
                if nums[i] < 0:
                    prods.append(1)
                elif nums[i] > 0:
                    prods.append(-1)
                else:
                    prods.append(0)
            elif prods[i-1] > 0:
                if nums[i] < 0:
                    prods.append(-1)
                elif nums[i] > 0:
                    prods.append(1)
                else:
                    prods.append(0)
           
        dp = [] # count since last zero
        if nums[0] == 0:
            dp.append(0)
        if nums[0] < 0:
            dp.append(1)
        if nums[0] > 0:
            dp.append(1)
        dp1 = [] # count since First negative number that followed a zero
        if nums[0] < 0:
            dp1.append(0)
        if nums[0] > 0:
            dp1.append(0)
        if nums[0] == 0:
            dp1.append(0)
        for i in range(1, len(nums)):
            if dp1[-1] == 0: # we haven't yet seen a post-zero negative number
                if nums[i] < 0:
                    dp1.append(1)
                else:
                    dp1.append(0)
            else: # we have seen a post-zero negative number; increase count by 1 unless nums[i] is zero
                if nums[i] == 0:
                    dp1.append(0)
                else:
                    dp1.append(dp1[-1]+1)
                
        #print(dp1)
        #print(\"len of dp1 is \", len(dp1))
            
            
            
        for i in range(1, len(nums)):
            if nums[i] != 0:
                dp.append(dp[i-1]+1)
            else:
                dp.append(0)
            if prods[i] > 0:
                maxProd = max(maxProd, dp[i])
            else:
                #print(\"i is \",i)
                if mostRecentPostZeroNeg[i] != float('-inf'):
                    maxProd = max(maxProd, i - mostRecentPostZeroNeg[i])
                #maxProd = max(maxProd, dp1[i]-1)
        #print(\"dp is \", dp)
        #print(\"dp1 is \", dp1)
        #print(\"zeroFound\", zeroFound)
        #print(\"mostRecentPost \", mostRecentPostZeroNeg)
        #print(\"prods are \", prods)
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
            else: # nums[i] > 0
                if dp[i-1] == 0:
                    if nums[i-1] == 0:
                        dp.append(1)
                    else:
                        dp.append(1)
                elif nums[i-1] < 0:
                    dp.append(dp[i-1] + 1)
                else: # nums[i-1] > 0
                    dp.append(dp[i-1] + 1)
            
            
        return dp[len(nums)-1]'''

