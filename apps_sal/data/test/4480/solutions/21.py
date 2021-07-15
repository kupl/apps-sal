class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if sum(A)-(sum(A)//3)*3!=0:
            return 0
        else:
            s=sum(A)//3
            c=0
            ts=0
            j=0
            for i in range(len(A)):
                j=i
                ts+=A[i]
                if ts==s:
                    c+=1
                    ts=0
                if c==2 and j+1<len(A):
                    for k in range(j+1,len(A)):
                        ts+=A[k]
                    if ts==s:
                        return 1
                    else:
                        return 0
            return 0

