class Solution:

    def primePalindrome(self, N: int) -> int:

        def isPrime(num):
            if num < 2:
                return False
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        for length in range(1, 6):
            for i in range(10 ** (length - 1), 10 ** length):
                num = str(i)
                palindrome = int(num + num[-2::-1])
                if palindrome >= N and isPrime(palindrome):
                    return min(palindrome, 11) if N <= 11 else palindrome
        return 0
