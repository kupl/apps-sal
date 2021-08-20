class Solution:

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        min1 = min2 = min3 = min4 = float('inf')
        max1 = max2 = max3 = max4 = float('-inf')
        for (i, [n1, n2]) in enumerate(zip(arr1, arr2)):
            (min1, max1) = (min(min1, n1 + n2 + i), max(max1, n1 + n2 + i))
            (min2, max2) = (min(min2, n1 + n2 - i), max(max2, n1 + n2 - i))
            (min3, max3) = (min(min3, n1 - n2 + i), max(max3, n1 - n2 + i))
            (min4, max4) = (min(min4, n1 - n2 - i), max(max4, n1 - n2 - i))
        return max(max1 - min1, max2 - min2, max3 - min3, max4 - min4)
