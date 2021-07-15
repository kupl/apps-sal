class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibo=[]
        fibo.append(1)
        fibo.append(1)
        lenn=2
        while fibo[-1]<=k:
            fibo.append(fibo[lenn-1]+fibo[lenn-2])
            lenn+=1
        
        nums=k
        cnt=0
        for i in range(len(fibo)-1, -1, -1):
            while nums>=fibo[i]:
                nums-=fibo[i]
                cnt+=1
            if nums==0:
                break
        return cnt
