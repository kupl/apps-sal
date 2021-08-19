(n, k) = map(int, input().split())
v = [int(x) for x in input().split()]
r = min(n, k)
ans = -10 ** 9
for i in range(r + 1):
    for j in range(r + 1):
        if i + j > r:
            continue
        l = sorted(v[:i] + v[::-1][:j])
        for a in range(k - (i + j) + 1):
            ans = max(ans, sum(l[a:]))
print(ans)
