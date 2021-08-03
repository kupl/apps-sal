class Solution:
    def is_prime(self, N):
        if N == 1:
            return False

        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                return False
        else:
            return True

    def primePalindrome(self, N: int) -> int:
        if N >= 8 and N <= 11:
            return 11
        for i in range(1, 100000):
            s = str(i)
            d = s[::-1]
            y = int(s + d[1:])
            if y >= N and self.is_prime(y):
                return y
