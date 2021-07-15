mod = 1000000007

class combination():
    def __init__(self, n):
        self.fact = [1] * (n+1)
        self.ifact = [1] * (n+1)
        for i in range(1, n+1):
            self.fact[i] = self.fact[i-1]*i % mod
        self.ifact[n] = pow(self.fact[n], mod-2, mod)
        for i in range(n, 0, -1):
            self.ifact[i-1] = self.ifact[i]*i % mod
    def comb(self, n, k):
        if k < 0 or k > n: return 0
        comb = self.fact[n]*self.ifact[k]*self.ifact[n-k] %mod
        return comb

def main():
    import sys
    input = sys.stdin.readline

    r1, c1, r2, c2 = map(int, input().split())

    comb = combination(2000010)

    # c1 ~ c2+1, r1 ~ r2+1
    ans = comb.comb(c2+r2+2, r2+1) - 1
    ans -= comb.comb(c1+r2+1, c1) - 1
    ans -= comb.comb(c2+r1+1, r1) - 1
    ans += comb.comb(c1+r1, r1) - 1
    print(ans % mod)

main()
