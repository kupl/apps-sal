def isPrime(val):
        if val==1:
            return False
        if val==2:
            return True
        if val%2==0:
            return False
        # print(floor(sqrt(val)))
        for i in range(3,floor(sqrt(val))+2,2):
            # print(i)
            if val%i == 0:
                return False
        return True
class Solution:
        
    def primePalindrome(self, N: int) -> int:
        if N>=8 and N<=11:
            return 11
        mn = 1e9
        # print(isPrime(N))
        for i in range(1,10009):
            s = str(i)
            r = s[::-1]
            # print(r)
            r = r[1:]
            # print(r)
            t = int(s+r)
            # print(t)
            if t>=N and isPrime(t):
                mn = min(mn,t)
        return mn
