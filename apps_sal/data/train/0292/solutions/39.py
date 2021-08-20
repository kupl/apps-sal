class Solution:

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        maxMax = (arr1[0] + arr2[0], 0)
        minMin = (-arr1[0] - arr2[0], 0)
        minMax = (-arr1[0] + arr2[0], 0)
        maxMin = (arr1[0] - arr2[0], 0)
        table = [maxMax, minMin, minMax, maxMin]
        n = len(arr1)
        ans = 0
        for i in range(1, n):
            for k in range(4):
                (_, j) = table[k]
                ans = max(ans, abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + i - j)
                if k == 0:
                    newSum = arr1[i] + arr2[i]
                elif k == 1:
                    newSum = -arr1[i] - arr2[i]
                elif k == 2:
                    newSum = -arr1[i] + arr2[i]
                elif k == 3:
                    newSum = arr1[i] - arr2[i]
                if newSum - 1 > table[k][0]:
                    table[k] = (newSum, i)
                else:
                    table[k] = (table[k][0] + 1, table[k][1])
        return ans
