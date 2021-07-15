class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        # dp = [[0 for i in range(len(A))] for j in range(len(len(A)))]
        ans = 0
        d={}
        for i in range(len(A)):
            d[A[i]] = 1
        
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                a = A[i]
                b = A[j]
                l=2
                while(d.get(a+b)!=None):
                    l+=1
                    temp = b
                    b = a+b
                    a = temp
                    
                ans = max(l,ans)
        
        if(ans>2):
            return ans
        return 0
                

