class Combination:
    def __init__(self, n, mod):
        self.n = n
        self.mod = mod
        self.fac = [1 for i in range(self.n + 1)]
        self.finv = [1 for i in range(self.n + 1)]
        for i in range(2, self.n+1):
            self.fac[i] = (self.fac[i - 1] * i) % self.mod
            self.finv[i] = (self.finv[i-1] * pow(i, -1, self.mod)) % self.mod

    def comb(self, n, m):
        return self.fac[n] * (self.finv[n-m] * self.finv[m] % self.mod) % self.mod
def iparse():
    return list(map(int, input().split()))

def __starting_point():
    s = input()
    ans = 0
    for i in range(1 << (len(s) - 1)):
        prev = 0
        for j in range(len(s) - 1):
            if (i >> j) & 1 == 1:
                tmp = s[prev:j + 1]
                ans += int(tmp)
                prev = j+1
        ans += int(s[prev:])
    print(ans)
            
        
    

__starting_point()
