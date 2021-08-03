class Solution:
    def primePalindrome(self, N: int) -> int:
        def isPrime(num):
            if num == 1:
                return False
            for div in range(2, int(num**0.5) + 1):
                if num % div == 0:
                    return False
            return True

        def isPalindrome(num):
            num = str(num)
            left = 0
            right = len(num) - 1
            while left < right:
                if num[left] != num[right]:
                    return False
                left += 1
                right -= 1
            return True

        while True:
            if isPalindrome(N) and isPrime(N):
                break
            N += 1
            if 10**7 < N < 10**8:
                N = 10**8
        return N
