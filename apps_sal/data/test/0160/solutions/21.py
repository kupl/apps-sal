n, k = map(int, input().split())
a = [int(x) for x in input().split()]
s = sum(a)

candidates = set()
for i in range(1, int(s**0.5) + 1):
    if s % i == 0:
        candidates.add(i)
        candidates.add(s // i)

ans = 0
for cdd in candidates:
    f = sorted([x % cdd for x in a])
    # calc need
    ans = max(ans, cdd) if sum(f[:-sum(f) // cdd]) <= k else ans

print(ans)
