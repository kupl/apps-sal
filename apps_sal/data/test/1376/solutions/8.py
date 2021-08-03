n = int(input())
a = list(map(int, input().split()))
a = [a[i] - 1 for i in range(2 * n)]
f = [-1] * n
l = [-1] * n
for i in range(2 * n):
    if f[a[i]] == -1:
        f[a[i]] = i
    else:
        l[a[i]] = i
ans = 0
cur = 0
for i in range(n):
    ans += abs(f[i] - cur)
    cur = f[i]
cur = 0
for i in range(n):
    ans += abs(l[i] - cur)
    cur = l[i]
print(ans)
