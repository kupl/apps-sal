class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0

        max4 = max3 = max2 = max1 = -float('inf')
        min4 = min3 = min2 = min1 = float('inf')

        for i in nums:
            if i > max1:
                max4 = max3
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2 and i <= max1:
                max4 = max3
                max3 = max2
                max2 = i
            elif i > max3 and i <= max2:
                max4 = max3
                max3 = i
            elif i > max4 and i <= max3:
                max4 = i

            if i < min1:
                min4 = min3
                min3 = min2
                min2 = min1
                min1 = i
            elif i < min2 and i >= min1:
                min4 = min3
                min3 = min2
                min2 = i
            elif i < min3 and i >= min2:
                min4 = min3
                min3 = i
            elif i < min4 and i >= min3:
                min4 = i

        smallest_diff = max4 - min1
        diff = max3 - min2
        if smallest_diff > diff:
            smallest_diff = diff
        diff = max2 - min3
        if smallest_diff > diff:
            smallest_diff = diff
        diff = max1 - min4
        if smallest_diff > diff:
            smallest_diff = diff
        return smallest_diff
    '''
    def minDifference(self, nums: List[int]) -> int:

        if len(nums) < 5: 
            return 0
        
        a = sorted(nums)
        
        H = len(nums) - 4
        L = 0
        lowest_diff = None
        for i in range(4):
            diff = a[H] - a[L]
            if lowest_diff == None or lowest_diff > diff:
                lowest_diff = diff
            H += 1
            L += 1
        
        return lowest_diff
    '''
    '''
    def minDifference(self, nums: List[int]) -> int:

        if len(nums) < 5: 
            return 0
        
        nums = sorted(nums)
        
        N = len(nums)
        lowest_diff = None
        for i in range(4):
            diff = nums[N-(4-i)] - nums[i]
            if lowest_diff == None or lowest_diff > diff:
                lowest_diff = diff
        
        return lowest_diff
    '''
    '''
    def minDifference(self, nums: List[int]) -> int:
        
        N = len(nums)
        
        if len(nums) < 5: 
            return 0
        
        a = sorted(nums)
        
        L = 0
        H = len(nums) - 1
        Lc = 0
        Hc = 0
        for i in range(3):
            m = int((L + H + 2)/2)
            M = a[m]
            low = a[L]
            high = a[H]
            lowDiff = M - low
            highDiff = high - M
            if lowDiff > highDiff:
                L += 1
                Lc += 1
            elif lowDiff < highDiff:
                H -= 1
                Hc += 1
            else:
                if Hc > Lc:
                    H -= 1
                    Hc += 1
                else:
                    L += 1
                    Lc += 1
                    
        return a[H] - a[L]
    '''
