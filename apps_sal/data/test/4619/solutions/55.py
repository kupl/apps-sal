class Combination:
    def __init__(self, n, mod):
        self.n = n
        self.mod = mod
        self.fac = [1 for i in range(self.n + 1)]
        self.finv = [1 for i in range(self.n + 1)]
        for i in range(2, self.n+1):
            self.fac[i] = (self.fac[i - 1] * i) % self.mod
            self.finv[i] = (self.finv[i - 1] * pow(i, -1, self.mod)) % self.mod

    def comb(self, n, m):
        return self.fac[n] * (self.finv[n - m] * self.finv[m] % self.mod) % self.mod
        
def iparse():
    return list(map(int, input().split()))


def __starting_point():
    w, h, n = iparse()
    xmax = w
    xmin = 0
    ymin = 0
    ymax = h
    for i in range(n):
        x, y, a = iparse()
        
        if a == 1:
            xmin = max(xmin,x)
        if a == 2:
            xmax = min(xmax,x)
        if a == 3:
            ymin = max(ymin,y)
        if a == 4:
            ymax = min(ymax,y)
        
    print((max(xmax-xmin,0)*(max(0,ymax-ymin))))
__starting_point()
