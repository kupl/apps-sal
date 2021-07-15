'''
Let g(x) = 序列內數字唯一，且最多 x 個位置不同。
Let f(x) = 序列內數字唯一，且給定 x 個位置時，使這些位置不同的方法數。

題目所求是 C(N, N) f(N)。

其中 g(x) 代表有至少 N - x 個位置是相同。可以分三個部份填數字，注意順序會影響，所以要乘上全排序：
(1) N - x 個位置（數字必需相同）：C(M, N - x) * (N - x)! = P(M, N - x)
(2) 序列 A 其餘位置（可以隨便填，但不能用到 (1) 的數字）：C(M - (N - x), x) * x! = P(M - (N - x), x)
(3) 序列 B 其餘位置（可以隨便填，但不能用到 (1) 的數字）：C(M - (N - x), x) * x! = P(M - (N - x), x)
g(x) = (1) * (2) * (3)

g(x) 是「選定 0 個位置，使這些位置不同的方法數」、「選定 1 個位置，使這些位置不同的方法數」、…、「選定 x 個位置，使這些位置不同的方法數」，即
g(x) = C(x, 0) f(0) + C(x, 1) f(1) + ... + C(x, x) f(x)
     = sum( C(x, i) * f(i) for i in [0, x] )
根據二項式反演，得到
f(x) = sum( (-1) ** (x - i) * C(x, i) * g(i) for i in [0, x] )
'''

class CombMod:
    def __init__(self, V, p):
        self.fact = [1] * V
        self.finv = [1] * V
        for i in range(1, V):
            self.fact[i] = self.fact[i - 1] * i % p
        self.finv[-1] = pow(self.fact[-1], p - 2, p)
        for i in range(V - 2, 0, -1):
            self.finv[i] = self.finv[i + 1] * (i + 1) % p
        self.p = p
        
    def fact(self, a):
        return self.fact[a]
    
    def finv(self, a):
        return self.finv[a]

    def comb(self, a, b):
        return self.fact[a] * self.finv[b] % self.p * self.finv[a - b] % self.p
        
    def perm(self, a, b):
        return self.fact[a] * self.finv[a - b] % self.p
    
    def hcomb(self, a, b):
        return self.comb(a + b - 1, b)


N, M = list(map(int, input().split()))
mod = 10**9 + 7
tool = CombMod(max(N, M) + 10, mod)

f_N = 0
for i in range(0, N + 1):
    p1 = tool.perm(M, N - i)
    p2 = tool.perm(M - (N - i), i)
    g_i = p1 * p2 % mod * p2 % mod
    val = (-1)**((N - i) % 2) * tool.comb(N, i) % mod * g_i % mod
    f_N = (f_N + val) % mod
ans = tool.comb(N, N) * f_N % mod
print(ans)

