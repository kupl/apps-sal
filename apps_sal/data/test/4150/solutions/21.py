n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
pre = {}
nex = {}
d = {}
for i in range(n):
    d[a[i]] = i
for i in range(n):
    pre[i] = i - 1
    nex[i] = i + 1

t = 1
ans = [-1] * n
for i in range(n, 0, -1):
    j = d[i]
    if ans[j] != -1:
        continue
    ans[j] = t
    l, r = pre[j], nex[j]
    for p in range(k):
        if l == -1:
            break
        ans[l] = t
        l = pre[l]

    for p in range(k):
        if r == n:
            break
        ans[r] = t
        r = nex[r]

    if l >= 0:
        nex[l] = r
    if r < n:
        pre[r] = l

    t = 3 - t

print(''.join(map(str, ans)))


