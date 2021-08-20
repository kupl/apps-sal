class Solution:

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        maxsize = 2147483647
        min1 = maxsize
        min2 = maxsize
        max1 = -maxsize - 1
        max2 = -maxsize - 1
        min3 = maxsize
        min4 = maxsize
        max3 = -maxsize - 1
        max4 = -maxsize - 1
        for i in range(len(arr1)):
            min1 = min(min1, arr1[i] + arr2[i] + i)
            max1 = max(max1, arr1[i] + arr2[i] + i)
            min2 = min(min2, arr1[i] + arr2[i] - i)
            max2 = max(max2, arr1[i] + arr2[i] - i)
            min3 = min(min3, arr1[i] - arr2[i] + i)
            max3 = max(max3, arr1[i] - arr2[i] + i)
            min4 = min(min4, arr1[i] - arr2[i] - i)
            max4 = max(max4, arr1[i] - arr2[i] - i)
        result = max(max1 - min1, max2 - min2, max3 - min3, max4 - min4)
        return result
