class Solution:
    def primePalindrome(self, N: int) -> int:

        # Brutal force over time limit
        if N == 1 or N == 2:
            return 2

        def isprime(k):
            j = 3
            while j * j <= k:
                if k % j == 0:
                    return False
                j += 2
            return True

        i = N // 2 * 2 + 1
        while i < 10**7:
            if str(i) == str(i)[::-1]:
                if isprime(i):
                    return i
            i += 2
        return 100030001
