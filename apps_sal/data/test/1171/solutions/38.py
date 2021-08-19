(n, k) = map(int, input().split())
v = list(map(int, input().split()))
m = min(n, k)
ans = 0
for i in range(m + 1):
    for j in range(m + 1 - i):
        l = []
        l = l + v[0:i] + v[n - j:n]
        l.sort()
        for kk in range(min(k - i - j, i + j)):
            if l[kk] < 0:
                l[kk] = 0
        ans = max(ans, sum(l))
print(ans)
