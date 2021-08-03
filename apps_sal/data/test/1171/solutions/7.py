n, k = map(int, input().split())
v = [int(x) for x in input().split()]

r = min(n, k)
ans = -10**9
for i in range(r + 1):
    for j in range(r + 1):
        if i + j > r:
            continue
        l = v[:i] + v[::-1][:j]
        m = sorted([l[x] for x in range(len(l)) if l[x] < 0])[:k - (i + j)]
        ans = max(ans, sum(l) - sum(m))

print(ans)
