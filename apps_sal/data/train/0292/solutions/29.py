class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        f1 = lambda i: arr1[i] + arr2[i] + i
        f2 = lambda i: -arr1[i] + arr2[i] + i
        f3 = lambda i: arr1[i] - arr2[i] + i
        f4 = lambda i: -arr1[i] - arr2[i] + i
        
        res = 0
        for f in [f1, f2, f3, f4]:
            low = float('inf')
            high = -float('inf')
            for i in range(len(arr1)):
                low = min(low, f(i))
                high = max(high, f(i))
            res = max(res, high - low)
        return res
