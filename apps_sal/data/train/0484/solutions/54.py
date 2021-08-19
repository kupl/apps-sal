class Solution:

    def primePalindrome(self, N: int) -> int:

        def prime(n):
            if n == 1:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        def reverse(N):
            res = 0
            d = N
            while N > 0:
                res = 10 * res + N % 10
                N = int(N / 10)
            return res
        while 1:
            if N == reverse(N) and prime(N):
                return N
            N += 1
            if 10 ** 7 < N < 10 ** 8:
                N = 10 ** 8
