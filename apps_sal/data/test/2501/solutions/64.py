n = int(input())
a = list(map(int, input().split()))
l = [i+a[i] for i in range(n)]
r = [i-a[i] for i in range(n)]
lc = {}
rc = {}
for i in range(n):
    lc[l[i]] = 0
    lc[r[i]] = 0
    rc[r[i]] = 0
    rc[l[i]] = 0
for i in range(n):
    lc[l[i]] += 1
    rc[r[i]] += 1
ans = 0
for i in set(lc.keys()):
    ans += rc[i]*lc[i]
print(ans)
