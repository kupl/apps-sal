n = int(input())
s = list(map(int, input().split()))
dist = []
p = [0 for i in range(100005)]
diff = 0
for i in range(n - 1, -1, -1):
    if p[s[i]] == 0:
        p[s[i]] = 1
        diff += 1
    else:
        p[s[i]] += 1
    dist += [diff]
vis = [0 for i in range(100005)]
ans = 0
for i in range(n - 1):
    if vis[s[i]] == 0:
        ans += dist[n - i - 2]
        vis[s[i]] = 1
print(ans)
