class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) == 1:
            return 1
        diff=0
        ret = 1
        max_ret = ret
        for i in range(len(A)-1):
            _diff=(A[i+1]-A[i])
            if diff*_diff <0:
                ret+=1
            else: 
                max_ret = max(ret,max_ret)
                if _diff == 0:
                    ret = 1
                else:
                    ret = 2
            diff = _diff
        return max(ret,max_ret)
