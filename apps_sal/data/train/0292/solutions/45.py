class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        ma = [float('-inf')] * 4
        res =[float('-inf')] * 4
        for i in range(n-1,-1,-1):
            a = [arr1[i] - arr2[i] + i,arr1[i] + arr2[i] + i,-arr1[i] + arr2[i] + i,-arr1[i] -arr2[i] + i]
            for j in range(4):
                res[j] = max(res[j], ma[j] - a[j])
            for j in range(4):
                ma[j] = max(ma[j], a[j])
        return max(res)

