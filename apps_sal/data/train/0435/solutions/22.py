class Solution:
    def TRIAlsubarraysDivByK(self, A: List[int], K: int) -> int:
        n = 0
        for i in range(len(A)):
            sum = 0
            for j in range(i,len(A)):
                sum+=A[j]
                if(sum%K==0):
                    n+=1
        return n
    
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        rems = [0]*len(A)
        for i in range(len(A)):
            if(i==0):
                rems[0] = A[0]%K
            else:
                rems[i] = (rems[i-1] + A[i])%K
        print(rems)
            
        count = list(Counter(rems).values())
        print(count)
        return(int(sum(n*(n-1)/2 for n in count)) + rems.count(0))

