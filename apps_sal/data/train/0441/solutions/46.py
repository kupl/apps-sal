'''
可能性：
1個數字：s
2個數字：s + s+1
3個數字：s + s+1 + s+2
...
n個數字：s + ...

=>
n
2n+1
3n+1+2
4n+1+2+3
...
=>
N = kn + (k-1 + 1)*(k-1)/2
=>
N = kn + (k**2-k)/2
=>
n = (N-(k**2-k)/2)/k
n>0且n為整數則符合

'''
class Solution1:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 0
        
        for k in range(1, 10**9):
            t = (k**2-k)/2
            s = (N-t)/k

            if s <= 0:
                break
            
            if s.is_integer():
                res += 1
        
        return res
# refactor
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 0
        
        for k in range(1, 10**9):
            s = N - (k*k-k)/2
            if s <= 0:
                break

            if s % k == 0:
                res += 1
                continue

        
        return res
