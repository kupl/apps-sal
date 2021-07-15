class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # 1. arr1[i] - arr1[j] + arr2[i] - arr2[j] + i - j => ( arr1[i] + arr2[i] + i) - ( arr1[j] + arr2[j] + j)
        # 2. arr1[i] - arr1[j] + arr2[i] - arr2[j] + j - i => ( arr1[i] + arr2[i] - i) - ( arr1[j] + arr2[j] - j)
        # 3. arr1[i] - arr1[j] + arr2[j] - arr2[i] + i - j => ( arr1[i] - arr2[i] + i) - ( arr1[j] - arr2[j] + j)
        # 4. arr1[i] - arr1[j] + arr2[j] - arr2[i] + j - i => ( arr1[i] - arr2[i] - i) - ( arr1[j] - arr2[j] - j)
        # 5. arr1[j] - arr1[i] + arr2[i] - arr2[j] + i - j => (-arr1[i] + arr2[i] + i) - (-arr1[j] + arr2[j] + j)
        # 6. arr1[j] - arr1[i] + arr2[i] - arr2[j] + j - i => (-arr1[i] + arr2[i] - i) - (-arr1[j] + arr2[j] - j)
        # 7. arr1[j] - arr1[i] + arr2[j] - arr2[i] + i - j => (-arr1[i] - arr2[i] + i) - (-arr1[j] - arr2[j] + j)
        # 8. arr1[j] - arr1[i] + arr2[j] - arr2[i] + j - i => (-arr1[i] - arr2[i] - i) - (-arr1[j] - arr2[j] - j)
        # min1, max1 for arr1[i] + arr2[i] + i
        # min2, max2 for arr1[i] + arr2[i] - i
        # min3, max3 for arr1[i] - arr2[i] + i
        # min4, max4 for arr1[i] - arr2[i] - i
        min1 = min2 = min3 = min4 = float('inf')
        max1 = max2 = max3 = max4 = float('-inf')
        for i in range(len(arr1)):
            s, d = arr1[i]+arr2[i], arr1[i]-arr2[i]
            min1, max1 = min(min1, s+i), max(max1, s+i)
            min2, max2 = min(min2, s-i), max(max2, s-i)
            min3, max3 = min(min3, d+i), max(max3, d+i)
            min4, max4 = min(min4, d-i), max(max4, d-i)
        return max(max1-min1, max2-min2, max3-min3, max4-min4)

