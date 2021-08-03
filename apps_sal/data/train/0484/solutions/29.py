class Solution:
    def primePalindrome(self, N: int) -> int:
        for i in range(N, 10**7 + 1):
            if not self.isPalindrome(i):
                continue
            if not self.isPrime(i):
                continue
            return i

        for i in range(10**8, 2 * 10**8):
            if not self.isPalindrome(i):
                continue
            if not self.isPrime(i):
                continue
            return i

    def isPalindrome(self, i):
        i = str(i)
        return i == i[::-1]

    def isPrime(self, i):
        return i > 1 and all([i % d != 0 for d in range(2, int(sqrt(i)) + 1)])
