class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        a = ''
        b = ''
       
        for i in range(len(A)):
            if A[i] != B[i]:
                a+=A[i]
                b+=B[i]
                
        return self.dfs(a,b)
        
    def dfs(self,a,b):
        if not a:
            return 0
        one = []
        two = []
        
        for i in range(len(a)):
            if a[0] == b[i]:
                one.append(i)
                if b[0] == a[i]:
                    two.append(i)
        
        if two:
            i = two[0]
            c = a[1:i] + a[i+1:]
            d = b[1:i] + b[i+1:]
            return self.dfs(c,d) + 1
        else:
            res = float('inf')
            for i in one:
                c = a[i] + a[1:i] + a[i+1:]
                d = b[:i]+b[i+1:]
                res= min(res,self.dfs(c,d)+1)
        
            return res

        
        
        
        
                
        

