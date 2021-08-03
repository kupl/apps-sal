class Solution:
    def primePalindrome(self, N: int) -> int:
        def checkPrime(x):
            if x == 1:
                return False

            for i in range(2, int(math.sqrt(x) + 0.01) + 1):
                if x % i == 0:
                    return False
            return True

        def makePal(n):
            l = len(n)
            hn = n[:l // 2]
            s = hn

            if l % 2 != 0:
                s += n[l // 2]

            return s + ''.join(reversed(hn))

        def nextPal(n):
            ni = int(n) + 10 ** (len(n) // 2)
            return makePal(str(ni))

        beg = str(N)
        n = makePal(beg)
        if n < beg:
            n = nextPal(n)

        while True:
            if checkPrime(int(n)):
                return int(n)
            n = nextPal(n)
