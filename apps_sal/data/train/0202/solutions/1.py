class Solution:
    def longestMountain(self, A: List[int]) -> int:
       
        leftpivot = 0
        rightpivot = 0
        ascendign = False
        descending = False
        changes = 0
        highest = 0
        while(leftpivot<len(A)):
            rightpivot=leftpivot
            
            if(rightpivot+1 < len(A) and A[rightpivot]<A[rightpivot+1]):
                while(rightpivot + 1<len(A) and A[rightpivot]<A[rightpivot+1] ):
                    rightpivot+=1


                if(rightpivot + 1<len(A) and A[rightpivot]>A[rightpivot+1]):
                    while(rightpivot<(len(A)-1) and A[rightpivot]>A[rightpivot+1]):
                        rightpivot+=1   
                    highest = max(highest,rightpivot+1-leftpivot)

            leftpivot = max(rightpivot,leftpivot+1)
        return highest

