def read(): return list(map(int, input().split()))


n, L = read()
c = list(read())
for _ in range(5):
    for i in range(n - 2, -1, -1):
        c[i] = min(c[i], c[i + 1])
    for i in range(1, n):
        c[i] = min(c[i], c[i - 1] * 2)
cur = 0
ans = 10 ** 30
L1 = L
for i in range(n - 1, -1, -1):
    cnt = L1 // (2**i)
    cur += cnt * c[i]
    ans = min(ans, cur + c[i])
    L1 -= cnt * (2**i)
ans = min(ans, cur)
for i in range(n - 1, -1, -1):
    if (2**i) >= L:
        ans = min(ans, c[i])
print(ans)
