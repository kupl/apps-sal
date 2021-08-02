n, m = map(int, input().split())
col = list(map(int, input().split()))
cs = set(col)
cnt = [None] * 100001
for i in range(100001):
    cnt[i] = set()
for i in range(m):
    u, v = map(int, input().split())
    if(col[u - 1] != col[v - 1]):
        cnt[col[u - 1]].add(col[v - 1])
        cnt[col[v - 1]].add(col[u - 1])
ans = -1
mx = -1
for i in range(100001):
    if(mx < len(cnt[i]) and i in cs):
        mx = len(cnt[i])
        ans = i
print(ans)
