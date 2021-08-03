class Solution:
    def primePalindrome(self, N: int) -> int:
        def reverse(n):
            return int(str(n)[::-1])

        def isPrime(n):
            return n > 1 and all(n % d for d in range(2, int(n**.5) + 1))

        while True:
            if N == reverse(N) and isPrime(N):
                return N
            N += 1
            if 10**7 < N < 10**8:
                N = 10**8
