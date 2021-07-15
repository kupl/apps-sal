class Solution:
    def primePalindrome(self, N: int) -> int:
        
        def isPrime(n):
            return n > 1 and all( n % f for f in range(2, int(n ** .5)+1) )
        
        def isPalin(n):
            tmp = str(n)
            return tmp == tmp[::-1]
        
        while True:
            if isPalin(N) and isPrime(N):
                return N
            
            N += 1
            if 12 <= N <= 99:
                N = 100
            elif 1000 <= N <= 9999:
                N = 10000
            elif 100000 <= N <= 999999:
                N = 1000000
            elif 10000000 <= N <= 99999999:
                N = 100000000
        

