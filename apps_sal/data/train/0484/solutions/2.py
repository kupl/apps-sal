class Solution:
    def primePalindrome(self, N: int) -> int:
        def checkPrime(x):
            if x == 1:
                return False

            for i in range(2, int(math.sqrt(x) + 0.01) + 1):
                if x % i == 0:
                    return False

            return True
        
        def makePal(ni):
            n = str(ni)
            l = len(n)
            hn = n[:l // 2]
            rhn = ''.join(reversed(hn))
            
            if l % 2 != 0:
                return int(hn + n[l // 2] + rhn)
            else:
                return int(hn + rhn)
                
        def nextPal(n):
            n = n + 10 ** (len(str(n)) // 2)
            return makePal(n)

        n = makePal(N)
        if n < N:
            n = nextPal(n)

        while True:
            if checkPrime(n):
                return n
            n = nextPal(n)
