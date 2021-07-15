class Solution:
    def primePalindrome(self, N: int) -> int:
        i = N
        while True:
            if self.isPalindrome(str(i)):
                if self.isPrime(i):
                    return i
            i += 1
            if 10**7 < i < 10**8:
                i = 10**8
            
    def isPalindrome(self, s):
        for i in range(0, len(s) // 2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

    def isPrime(self, n):
        if n < 2 or len(str(n)) == 8:
            return False
        
        upper = int(sqrt(n))
        for i in range(2, upper+1):
            if n % i == 0:
                return False
        return True

        # return True

