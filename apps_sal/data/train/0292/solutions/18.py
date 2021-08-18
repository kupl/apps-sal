
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        max1 = max2 = max3 = max4 = -math.inf
        min1 = min2 = min3 = min4 = math.inf
        for i in range(len(arr1)):
            x = arr1[i]
            y = arr2[i]
            max1 = max(max1, x + y - i)
            min1 = min(min1, x + y - i)

            max2 = max(max2, x - y - i)
            min2 = min(min2, x - y - i)

            max3 = max(max3, -x + y - i)
            min3 = min(min3, -x + y - i)

            max4 = max(max4, -x - y - i)
            min4 = min(min4, -x - y - i)

        return max(max1 - min1, max2 - min2, max3 - min3, max4 - min4)
