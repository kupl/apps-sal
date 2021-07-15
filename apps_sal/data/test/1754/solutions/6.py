n, m, k = map(int, input().split())
s = list(map(int, input().split()))
p = list(map(int, input().split()))
c = list(map(int, input().split()))

maxs = [0 for i in range(m)]
for i in range(n):
    maxs[p[i] - 1] = \
        max(maxs[p[i] - 1],
            s[i])
ans = 0
for x in c:
    if s[x - 1] != maxs[p[x - 1] - 1]:
        ans += 1
print(ans)
