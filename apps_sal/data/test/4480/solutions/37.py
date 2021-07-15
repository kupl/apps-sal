class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        l,r,s=1, len(A)-2, sum(A)
        ls, rs, avgs = A[0], A[-1], s//3
        while l<r:
            if l < r and ls != avgs:
                ls+=A[l]
                l+=1
            if l<r and rs!=avgs:
                rs+=A[r]
                r-=1
            if ls == rs == avgs and s%3==0:
                return True
            
        return False
