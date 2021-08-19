(n, m, k) = map(int, input().split())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
c = list(map(int, input().split()))
d = [[] for i in range(m)]
for i in range(n):
    d[s[i] - 1].append((p[i], i + 1))
for i in range(m):
    d[i].sort(reverse=True)
ans = 0
for i in range(m):
    if d[i][0][1] in c:
        ans += 1
print(k - ans)
