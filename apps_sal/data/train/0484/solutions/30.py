class Solution:

    def primePalindrome(self, N: int) -> int:
        if N == 1:
            return 2

        def isPrime(num):
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        while str(N) != str(N)[::-1] or not isPrime(N):
            N += 1
            if 10 ** 7 < N < 10 ** 8:
                N = 10 ** 8
        return N
