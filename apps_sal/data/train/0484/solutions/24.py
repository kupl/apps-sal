class Solution:

    def primePalindrome(self, N: int) -> int:

        @lru_cache(None)
        def isPrime(n):
            if n == 1:
                return False
            for i in range(2, int(sqrt(n)) + 1):
                if isPrime(i):
                    if n % i == 0:
                        return False
            return True

        def isPalindrome(n):
            return n == int(str(n)[::-1])
        while True:
            if isPalindrome(N) and isPrime(N):
                return N
            N += 1
            length = len(str(N))
            if length > 2 and length % 2 == 0:
                N = int('1' + '0' * (length - 1) + '1')
        return None
