class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        x, y = arr1, arr2
        maxCase1 = maxCase2 = maxCase3 = maxCase4 = -float('inf')
        minCase1 = minCase2 = minCase3 = minCase4 = float('inf')
        for i in range(len(x)):
            maxCase1 = max(maxCase1, x[i]+y[i]-i)
            maxCase2 = max(maxCase2, x[i]-y[i]-i)
            maxCase3 = max(maxCase3, -x[i]+y[i]-i)
            maxCase4 = max(maxCase4, -x[i]-y[i]-i)
            minCase1 = min(minCase1, x[i]+y[i]-i)
            minCase2 = min(minCase2, x[i]-y[i]-i)
            minCase3 = min(minCase3, -x[i]+y[i]-i)
            minCase4 = min(minCase4, -x[i]-y[i]-i)
        return max(maxCase1-minCase1, maxCase2-minCase2, maxCase3-minCase3, maxCase4-minCase4)
