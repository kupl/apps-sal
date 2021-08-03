class Solution:
    def primePalindrome(self, N: int) -> int:

        def isprime(i):
            if i == 1:
                return False
            for j in range(2, int(i**(0.5)) + 1):
                if i % j == 0:
                    return False
            return True

        i = N
        while i < 2 * (10**10):
            x = str(i)
            if len(x) % 2 == 0 and len(x) > 2:
                i = 10 ** (len(x))
                continue
            elif x == x[::-1]:
                if isprime(i):
                    return i
            i += 1
