class Solution:
    def primePalindrome(self, N: int) -> int:
        def check_p(n):
            return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))
        while True:
            if str(N) == str(N)[::-1] and check_p(N):
                return N
            N += 1
            if 10**8 > N > 10**7:
                N = 10**8
