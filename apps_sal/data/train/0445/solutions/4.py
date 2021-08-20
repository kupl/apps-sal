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
    '\n    #original submission\n    def minDifference(self, nums: List[int]) -> int:\n\n        if len(nums) < 5: \n            return 0\n        \n        a = sorted(nums)\n        \n        H = len(nums) - 4\n        L = 0\n        lowest_diff = None\n        for i in range(4):\n            diff = a[H] - a[L]\n            if lowest_diff == None or lowest_diff > diff:\n                lowest_diff = diff\n            H += 1\n            L += 1\n        \n        return lowest_diff\n    '
    '\n    # faster and cleaner - same as original solution\n    def minDifference(self, nums: List[int]) -> int:\n\n        if len(nums) < 5: \n            return 0\n        \n        nums = sorted(nums)\n        \n        N = len(nums)\n        lowest_diff = None\n        for i in range(4):\n            diff = nums[N-(4-i)] - nums[i]\n            if lowest_diff == None or lowest_diff > diff:\n                lowest_diff = diff\n        \n        return lowest_diff\n    '
    "\n    #original attempt - sort into a sort of binary search\n    def minDifference(self, nums: List[int]) -> int:\n        \n        N = len(nums)\n        \n        # any array of length 4 or less can have all elements mapped to same value\n        if len(nums) < 5: \n            return 0\n        \n        # sort \n        a = sorted(nums)\n        \n        # compare 'new' low/highs to an updated median\n        L = 0\n        H = len(nums) - 1\n        # counts for those remapped from each side\n        Lc = 0\n        Hc = 0\n        for i in range(3):\n            m = int((L + H + 2)/2)\n            M = a[m]\n            low = a[L]\n            high = a[H]\n            lowDiff = M - low\n            highDiff = high - M\n            # implies we should set the lowest value to the final median\n            if lowDiff > highDiff:\n                L += 1\n                Lc += 1\n            # implies we should set the highest value to the final median\n            elif lowDiff < highDiff:\n                H -= 1\n                Hc += 1\n            # implies the differences are the same - pick the side with a higher count\n            else:\n                if Hc > Lc:\n                    H -= 1\n                    Hc += 1\n                else:\n                    L += 1\n                    Lc += 1\n                    \n        return a[H] - a[L]\n    "
