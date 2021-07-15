class Solution:
    def countTriplets(self, A: List[int]) -> int:
        count=0
        dic=dict()
        for i in range(len(A)):
            for j in range(i,len(A)):
                r=A[i]&A[j]
                dic[r]=dic.get(r,0)+(1 if i==j else 2)
        result=0
        for i in range(len(A)):
            for k in dic:
                if A[i]&k==0:
                    result+=dic[k]
                
        return result
                    

