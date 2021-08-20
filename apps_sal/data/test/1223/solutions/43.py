import bisect
n = int(input())
p = [int(x) - 1 for x in input().split()]
p2 = sorted(enumerate(p), key=lambda x: x[1], reverse=True)
ans = 0
s = [-1, -1, n, n]
for (i, (idx, p)) in enumerate(p2):
    t = bisect.bisect_left(s, idx)
    s.insert(t, idx)
    l1 = s[t - 1]
    l2 = s[t - 2]
    r1 = s[t + 1]
    r2 = s[t + 2]
    ans += (p + 1) * ((idx - l1) * (r2 - r1) + (r1 - idx) * (l1 - l2))
print(ans)
