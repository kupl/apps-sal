(H, W, A, B) = map(int, input().split())
MAX_NUM = 2 * 10 ** 5 + 1
pr = 10 ** 9 + 7
fac = [0 for _ in range(MAX_NUM)]
finv = [0 for _ in range(MAX_NUM)]
inv = [0 for _ in range(MAX_NUM)]
fac[0] = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1
for i in range(2, MAX_NUM):
    fac[i] = fac[i - 1] * i % pr
    inv[i] = pr - inv[pr % i] * (pr // i) % pr
    finv[i] = finv[i - 1] * inv[i] % pr


def c(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % pr) % pr


a = 0
while 1:
    a = (a + c(H - A - 1 + B, B) * c(A + W - B - 1, A)) % pr
    A += 1
    B += 1
    if A == H or B == W:
        break
print(a)
