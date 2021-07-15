class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        d = {}
        def steps(num, level):
#             if num in d:
#                 return d[num] + level
            
#             d[num] = level
            if num==1:
                return level
            if num%2==0:
                return steps(num/2, level+1)
            else:
                return steps(3*num+1, level+1)
            
        ans = [(steps(x,0), x) for x in range(lo,hi+1)]
        ans.sort()
        return ans[k-1][-1]
