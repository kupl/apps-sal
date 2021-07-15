H, W, A, B = [int(_) for _ in input().split()]
mod = 10**9 + 7
 
X = [i for i in range(H + W + 1)]
X[0] = 1
for i in range(2, H + W + 1):
    X[i] = X[i - 1] * i % mod
 
Y = X.copy()
Y[-1] = pow(Y[-1], mod - 2, mod)
for i in range(H + W, 1, -1):
    Y[i - 1] = i * Y[i] % mod
 
 
def comb(x, y):
    return X[x] * Y[y] * Y[x - y] % mod
 
 
ans = 0
for i in range(B, min(B + H - A, W)):
    ans += comb(H - A + B - 1, i) * comb(W + A - B - 1, W - i - 1)
    ans %= mod
print(ans)
