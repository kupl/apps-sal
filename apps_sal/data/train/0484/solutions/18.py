class Solution:
    def primePalindrome(self, N: int) -> int:
        if N < 12:
            for i in range(1, 12):
                if self.isPrime(i) and i >= N:
                    return i
        strN = str(N)
        strLen = len(strN)
        if strLen % 2 == 0:
            startPoint = 10 ** (strLen // 2)
        else:
            startPoint = int(strN[:strLen // 2 + 1])
        for point in range(startPoint, 10**6):
            strPoint = str(point)
            palindrome = int(strPoint + strPoint[-2::-1])
            if palindrome >= N and self.isPrime(palindrome):
                return palindrome

    def isPrime(self, p):
        return p > 1 and all(p % d for d in range(2, int(p**0.5) + 1))
