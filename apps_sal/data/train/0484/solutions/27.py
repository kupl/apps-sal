class Solution:

    def primePalindrome(self, N: int) -> int:

        def is_prime(num):
            return num > 1 and all(num % d for d in range(2, int(num**0.5) + 1))

        while True:
            if str(N) == str(N)[::-1] and is_prime(N):
                return N
            N += 1
            if 10**7 < N < 10**8:
                N = 10**8
