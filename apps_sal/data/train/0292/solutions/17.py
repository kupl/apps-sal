class Solution:
    def calc(self, a, b):
        c = [ai+bi for ai, bi in zip(a, b)]
        m = 10**18
        res = 0
        
        for i in range(len(c)):
            m = min(m, c[i]+i)
            res = max(res, c[i]+i-m)
            
        return res
    
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        arr1_ = [-arr1_i for arr1_i in arr1]
        arr2_ = [-arr2_i for arr2_i in arr2]
        return max(self.calc(arr1, arr2), self.calc(arr1, arr2_), self.calc(arr1_, arr2), self.calc(arr1_, arr2_))
