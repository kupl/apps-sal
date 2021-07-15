class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1,1]
        while(fib[-1]<k):
            fib.append(fib[-1]+fib[-2])
        print(fib)
        if k in fib:
            return 1
        cnt =0
        for i in range(len(fib)-1,-1,-1):
            print(('cnt ',cnt,'i ',i, fib[i],'k ',k))
            if fib[i]<=k:
                k = k-fib[i]
                cnt+=1
            if k==0:
                break
        return cnt
            
        

