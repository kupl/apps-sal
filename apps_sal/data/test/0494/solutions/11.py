n, m = list(map(int, input().split()))
l = list(map(int, input().split()))
used = [False for _ in range(n + 1)]
ans = [0 for _ in range(n)]
f = True
for i in range(m - 1):
    d = ((l[i + 1] - l[i] + n - 1) % n) + 1
    if ans[l[i] - 1] == 0 and not used[d]:
        ans[l[i] - 1] = d
        used[d] = True
    elif ans[l[i] - 1] != d:
        f = False
        break

s = 0
j = 1
for i in range(n):
    while j < n and used[j]:
        j += 1
    if ans[i] == 0:
        ans[i] = j
        used[j] = True
    s += ans[i]

if s != n * (n + 1) // 2:
    f = False

idx = l[0] - 1
for i in range(m):
    if idx + 1 != l[i]:
        f = False
        break
    idx += ans[idx]
    idx %= n

if f:
    print(' '.join(list(map(str, ans))))
else:
    print(-1)
