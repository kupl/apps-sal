mod = 998244353
(n, k) = map(int, input().split())
L = []
R = []
for _ in range(k):
    (l, r) = map(int, input().split())
    L.append(l)
    R.append(r)
sdp = [1]


def f(x):
    if x < 0:
        return 0
    else:
        return sdp[x]


for i in range(1, n):
    x = 0
    for j in range(k):
        x += f(i - L[j]) + mod - f(i - R[j] - 1)
        x %= mod
    sdp.append((x + sdp[i - 1]) % mod)
print((sdp[n - 1] + mod - sdp[n - 2]) % mod)
