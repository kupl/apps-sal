class Solution:
    
    def minDays(self, n: int) -> int:
        def recur(n: int) -> int:
            if n <= 1:
                return n;
            if n>=self.N or self.arr[n]==-1: 
                ans=1 + min(n % 2 + recur(n // 2), n % 3 + recur(n // 3))
                if n<self.N: self.arr[n]=ans
            else:
                ans=self.arr[n]
            return ans;   
    
        self.N=min(100000,n)
        self.arr=[-1]*self.N

        return recur(n)
