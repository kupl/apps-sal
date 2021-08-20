class Solution:

    def primePalindrome(self, N: int) -> int:

        def reverse(n):
            sm = 0
            while n > 0:
                r = n % 10
                sm = sm * 10 + r
                n = n // 10
            return sm

        def isprime(n):
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        if N == 1:
            return 2
        while True:
            if N == reverse(N) and isprime(N):
                return N
            N += 1
            if 10 ** 7 < N < 10 ** 8:
                N = 10 ** 8
