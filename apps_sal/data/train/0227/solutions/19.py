class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        count=0
        maxCount=-1
        first=0
        for i in range(len(A)):
            if A[i]==0 and K!=0:
                count+=1
                K-=1
            elif A[i]==0 and K==0:
                while A[first]!=0:
                    first+=1
                    count-=1
                first+=1
            else:
                count+=1
            maxCount=max(maxCount,count)
        return maxCount
            

