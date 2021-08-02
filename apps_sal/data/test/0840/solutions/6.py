def read(): return list(map(int, input().split()))


n, k = read()
a = list(read())
b = list(read())
c = [0] * n
r = [0] * n
for i in range(n):
    c[i] = b[i] // a[i]
    r[i] = a[i] - b[i] % a[i]


def f(x):
    k1 = k
    for i in range(n):
        if c[i] >= x:
            continue
        cnt = (x - c[i] - 1) * a[i] + r[i]
        k1 -= cnt
        if k1 < 0:
            return False
    return True


L, R = 0, 10 ** 10
while R - L > 1:
    M = (L + R) // 2
    if f(M):
        L = M
    else:
        R = M
ans = L
print(ans)
