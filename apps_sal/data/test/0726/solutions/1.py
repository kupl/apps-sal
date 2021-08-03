n, d = list(map(int, input().split()))
a = list(map(int, input().split()))


cands = set()
for x in a:
    cands.add(x - d)
    cands.add(x + d)

ans = 0
for x in cands:
    mn_dist = min([abs(t - x) for t in a])
    ans += mn_dist == d

print(ans)
