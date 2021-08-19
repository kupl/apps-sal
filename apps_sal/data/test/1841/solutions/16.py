(n, m) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
s = [0] * (10 ** 5 + 1)
ans = [0] * n
for i in range(n):
    if not s[a[n - 1 - i]]:
        s[a[n - 1 - i]] = 1
        ans[n - 1 - i] = 1
for i in range(n - 1):
    ans[n - 2 - i] += ans[n - 1 - i]
res = []
for i in range(m):
    res.append(str(ans[int(input()) - 1]))
print('\n'.join(res))
