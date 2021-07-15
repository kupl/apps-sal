class Solution:
     res=[1]
     idx=[0,0,0]
     def nthUglyNumber(self, n):
         """
         :type n: int
         :rtype: int
         """
         if n<=0:
             return None
         idx2,idx3,idx5=Solution.idx
         while len(Solution.res)<n:
             Solution.res.append(min(Solution.res[idx2]*2,Solution.res[idx3]*3,Solution.res[idx5]*5))
             while idx2<len(Solution.res) and Solution.res[idx2]*2<=Solution.res[-1]:
                 idx2+=1
             while idx3<len(Solution.res) and Solution.res[idx3]*3<=Solution.res[-1]:
                 idx3+=1
             while idx5<len(Solution.res) and Solution.res[idx5]*5<=Solution.res[-1]:
                 idx5+=1
         Solution.idx=[idx2,idx3,idx5]
         return Solution.res[n-1]

