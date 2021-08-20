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
    '\n    # faster and cleaner\n    def minDifference(self, nums: List[int]) -> int:\n\n        if len(nums) < 5: \n            return 0\n        \n        nums = sorted(nums)\n        \n        N = len(nums)\n        lowest_diff = None\n        for i in range(4):\n            diff = nums[N-(4-i)] - nums[i]\n            if lowest_diff == None or lowest_diff > diff:\n                lowest_diff = diff\n        \n        return lowest_diff\n    '
    "\n    #original attempt\n    def minDifference(self, nums: List[int]) -> int:\n        \n        N = len(nums)\n        \n        # any array of length 4 or less can have all elements mapped to same value\n        if len(nums) < 5: \n            return 0\n        \n        # sort \n        a = sorted(nums)\n        \n        # compare 'new' low/highs to an updated median\n        L = 0\n        H = len(nums) - 1\n        # counts for those remapped from each side\n        Lc = 0\n        Hc = 0\n        for i in range(3):\n            m = int((L + H + 2)/2)\n            M = a[m]\n            low = a[L]\n            high = a[H]\n            lowDiff = M - low\n            highDiff = high - M\n            # implies we should set the lowest value to the final median\n            if lowDiff > highDiff:\n                L += 1\n                Lc += 1\n            # implies we should set the highest value to the final median\n            elif lowDiff < highDiff:\n                H -= 1\n                Hc += 1\n            # implies the differences are the same - pick the side with a higher count\n            else:\n                if Hc > Lc:\n                    H -= 1\n                    Hc += 1\n                else:\n                    L += 1\n                    Lc += 1\n                    \n        return a[H] - a[L]\n    "
