MOD = 10**9 + 7
class mint:
    def __init__(self, i):
        self.i = i
    def __add__(self, m):
        t = self.i + (m.i if isinstance(m, mint) else m)
        if t > MOD:
            t -= MOD
        return mint(t)
    def __radd__(self, m):
        t = self.i + (m.i if isinstance(m, mint) else m)
        if t > MOD:
            t -= MOD
        return mint(t)
    def __mul__(self, m):
        return mint(self.i * (m.i if isinstance(m, mint) else m) % MOD)
    def __sub__(self, m):
        t = self.i - m.i
        if t < 0:
            t += MOD
        return mint(t)
    def __pow__(self, m):
        i = self.i
        res = 1
        while(m > 0):
            if m & 1:
                res = res * i % MOD 
            i = i * i % MOD
            m >>= 1
        return mint(res)
    def __truediv__(self, m):
        return mint(self.i * (m ** (MOD - 2)).i % MOD)
    def __repr__(self):
        return repr(self.i)

L, R = map(int, input().split())
dp = [[mint(0) for _ in range(4)] for _ in range(61)]

for d in range(60, 0, -1):
    l = L >> d - 1 & 1
    r = R >> d - 1 & 1
    
    if (L >> d - 1) == 0:
        if (R >> d - 1) > 1:
            dp[d-1][3] += 1
        elif (R >> d - 1) == 1:
            dp[d-1][2] += 1
    elif (L >> d - 1) == 1:
        if (R >> d - 1) > 1:
            dp[d-1][1] += 1
        else:
            dp[d-1][0] += 1

    # x bound, y bound
    if l == r:
        dp[d-1][0] += dp[d][0]
    elif l < r:
        dp[d-1][0] += dp[d][0]
        dp[d-1][1] += dp[d][0]
        dp[d-1][2] += dp[d][0]
    # x bound, y free
    if l == 0:
        dp[d-1][1] += dp[d][1] * 2
        dp[d-1][3] += dp[d][1]
    else:
        dp[d-1][1] += dp[d][1]
    # x free, y bound
    if r == 1:
        dp[d-1][2] += dp[d][2] * 2
        dp[d-1][3] += dp[d][2]
    else:
        dp[d-1][2] += dp[d][2]
    # x free, y free
    dp[d-1][3] += dp[d][3] * 3

print(sum(dp[0]))
