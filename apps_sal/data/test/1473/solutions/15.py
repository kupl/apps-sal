n = int(input())
maxn = 10 ** 6 + 1
nxt = [0] * maxn
nxta = [0] * maxn
ans = [0] * n
used = [0] * maxn
for i in range(n):
    x, y = map(int, input().split())
    if x == 0:
        s = i
    nxta[x] = i
    nxt[i] = y
    used[x] += 1
    used[y] += 2
for i in range(maxn):
    if used[i] == 1:
        z = i
for i in range(n):
    ans[i] = z
    z, s = nxt[s], nxta[z]
for i in ans:
    print(i, end=' ')
