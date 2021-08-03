class Solution:
    def primePalindrome(self, N: int) -> int:

        def isprime(N):
            if N <= 1:
                return False
            n = 2
            while n <= N**.5:
                if N % n == 0:
                    return False
                n += 1
            return True

        def ispali(N):
            s = str(N)
            i, j = 0, len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        while 1:
            if ispali(N):
                if isprime(N):
                    return N
            N += 1
            if 10**7 < N < 10**8:
                N = 10**8
