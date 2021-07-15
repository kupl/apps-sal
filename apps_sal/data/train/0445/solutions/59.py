class Solution:
    #original submission
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
    # faster and cleaner
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
    #original attempt
    def minDifference(self, nums: List[int]) -> int:
        
        N = len(nums)
        
        # any array of length 4 or less can have all elements mapped to same value
        if len(nums) < 5: 
            return 0
        
        # sort 
        a = sorted(nums)
        
        # compare 'new' low/highs to an updated median
        L = 0
        H = len(nums) - 1
        # counts for those remapped from each side
        Lc = 0
        Hc = 0
        for i in range(3):
            m = int((L + H + 2)/2)
            M = a[m]
            low = a[L]
            high = a[H]
            lowDiff = M - low
            highDiff = high - M
            # implies we should set the lowest value to the final median
            if lowDiff > highDiff:
                L += 1
                Lc += 1
            # implies we should set the highest value to the final median
            elif lowDiff < highDiff:
                H -= 1
                Hc += 1
            # implies the differences are the same - pick the side with a higher count
            else:
                if Hc > Lc:
                    H -= 1
                    Hc += 1
                else:
                    L += 1
                    Lc += 1
                    
        return a[H] - a[L]
    '''
