class Solution:
    def primePalindrome(self, N: int) -> int:
        def ispad(n):
            n = str(n)
            n = list(n)
            left, right = 0,len(n)-1
            while left < right:
                if n[left] != n[right]:
                    return False
                left += 1
                right -= 1
            return True
            
        
        def isprime(n):
            for i in range(2, int(n**.5)+1):
                if n%i==0:
                    return False
            return True
        
        if N==1:
            return 2
        
        while True:
            if ispad(N) and isprime(N):
                return N
            N+=1
            if 10**7 < N < 10**8:
                N = 10**8

