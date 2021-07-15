n = int(input())
c = [0] * n
s = [0] * n
f = [0] * n
for i in range(n - 1):
    c[i], s[i], f[i] = map(int, input().split())

ans = [0] * n
for i in range(n - 1):
    for j in range(i, n - 1):
        if ans[i] < s[j]:
            ans[i] = s[j]
        elif ans[i] % f[j] > 0:
            ans[i] += f[j] - ans[i] % f[j]
        ans[i] += c[j]

for i in range(n):
    print(ans[i])
