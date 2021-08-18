class Solution:
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
