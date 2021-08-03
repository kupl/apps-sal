n, m = list(map(int, input().split()))
mod = 10**9 + 7

B = [1]
W = [1]
BB = [0]
WW = [0]

for i in range(1, 100010):
    x = W[-1] + WW[-1]
    y = B[-1] + BB[-1]
    z = B[-1]
    w = W[-1]

    x %= mod
    y %= mod
    z %= mod
    w %= mod

    B.append(x)
    W.append(y)
    BB.append(z)
    WW.append(w)

print((B[n - 1] + W[n - 1] + BB[n - 1] + WW[n - 1] + B[m - 1] + W[m - 1] + BB[m - 1] + WW[m - 1] - 2) % mod)
