class Solution:
    def superPow(self, a, b):
        num = 0
        currentpow = 1
        for item in b[::-1]:
            num += currentpow * item
            currentpow *= 10
        return self.binpow(a, num % 570)

    def binpow(self, n, p):
        if(p == 0):
            return 1
        if(p % 2 == 0):
            return (self.binpow(n * n, p // 2)) % 1337
        return (n * self.binpow(n, p - 1)) % 1337
