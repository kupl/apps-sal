import math
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        a=N
        while a%2==0:
            a=a//2
        s=math.sqrt(a)
        i=1
        ans=0
        while i<s:
            if a%i==0:
                ans+=1
            i+=2
        if i*i==a:
            return 2*ans+1
        else:
            return 2*ans
