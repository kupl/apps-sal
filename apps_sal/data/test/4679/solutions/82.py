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
    s = [list(input()) for i in range(3)]
    for e in s:
        e.reverse()
    
    turn = 0
    while True:
        if len(s[turn]) == 0:
            break
        tmp = s[turn].pop()
        if tmp == 'a':
            turn = 0
        elif tmp == 'b':
            turn = 1
        else:
            turn = 2

    if turn == 0:
        print("A")
    elif turn == 1:
        print("B")
    else:
        print("C")
        
    

__starting_point()
