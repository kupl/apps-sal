class Solution:
    def primePalindrome(self, N: int) -> int:
        def isPrime(n):
            if n > 1:
                if n == 2:
                    return True
                if n % 2 == 0:
                    return False
                for x in range(3, int(n**.5 + 1), 2):
                    if n % x == 0:
                        return False
                return True
            return False

        def nextPalind(N):
            i = N + 1
            while True:
                if str(i) == str(i)[::-1]:
                    return i
                else:
                    i += 1
        if N >= 9989900:
            return 100030001

        if isPrime(N) and (str(N) == str(N)[::-1]):
            return N
        else:
            i = nextPalind(N)
            while not isPrime(i):
                i = nextPalind(i)
            return i
