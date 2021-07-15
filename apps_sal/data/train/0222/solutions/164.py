class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        if len(A)<3:
            return 0
        dic={}
        m=max(A)
        for i in range(len(A)):
            dic[A[i]]=1
        m=0
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                c=2
                a=A[i]
                b=A[j]
                try:
                    while dic[a+b]==1:
                        temp=b
                        b=a+b
                        a=temp
                        c+=1
                except KeyError:
                    m=max(m,c)
                m=max(m,c)
        if m<3:
            return 0
        return m

