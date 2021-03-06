class Solution:

    def primePalindrome(self, N: int) -> int:

        def is_prime(n):
            return n > 1 and all((n % d != 0 for d in range(2, int(n ** 0.5) + 1)))

        def reverse(x):
            y = 0
            while x > 0:
                y = y * 10 + x % 10
                x = x // 10
            return y
        while True:
            if N == reverse(N) and is_prime(N):
                return N
            N += 1
            if 10 ** 7 < N < 10 ** 8:
                N = 10 ** 8
