mod = 998244353
pws = [1]
for i in range(1, 22):
    pws.append(pws[i - 1] * 10)
n = int(input())
h = list(map(int, input().split()))
a = [[] for i in range(n)]
for i in range(n):
    x = h[i]
    while x:
        a[i].append(x % 10)
        x = x // 10
cnt = [0] * 11
for i in range(n):
    cnt[len(a[i])] += 1
s = 0
for i in range(n):
    for j in range(len(a[i])):
        cur = 0
        for k in range(1, j):
            s = (s + a[i][j] * pws[j + k] * cnt[k]) % mod
            cur += cnt[k]
        s = (s + a[i][j] * pws[2 * j] * (n - cur)) % mod
        cur = 0
        for k in range(1, j + 1):
            s = (s + a[i][j] * pws[j + k] * cnt[k]) % mod
            cur += cnt[k]
        s = (s + a[i][j] * pws[2 * j + 1] * (n - cur)) % mod
print(s)
