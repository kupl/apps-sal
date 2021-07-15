MOD = 998244353
n, m = list(map(int, input().split()))
d = dict()
a = [0] + list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(m):
    d[b[i]] = i
c = [-1] * m
for i, x in enumerate(a):
    if x in d:
        c[d[x]] = i
idx = n
ans = 1
for i in range(m - 1, -1, -1):
    while b[i] <= a[idx]:
        idx -= 1
    if c[i] <= idx:
        print(0)
        return
    if i > 0:
        ans *= c[i] - idx
    elif idx > 0:
        print(0)
        return
    ans %= MOD
print(ans)

