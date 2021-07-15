class Solution:
    def helper(self,sign1, sign2, arr1, arr2):
        m1, m2 = -10**7, 10**7

        for i in range(len(arr1)):
            t = sign1*arr1[i] + sign2*arr2[i] + i
            m1 = max(m1,t)
            m2 = min(m2,t)

        return m1 - m2


    def maxAbsValExpr(self, arr1, arr2):
        res = 0

        res = max(res,self.helper(1,1,arr1,arr2))
        res = max(res,self.helper(-1,1,arr1,arr2))
        res = max(res,self.helper(1,-1,arr1,arr2))
        res = max(res,self.helper(-1,-1,arr1,arr2))

        return res
