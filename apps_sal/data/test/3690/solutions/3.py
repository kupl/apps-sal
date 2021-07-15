h, m, s, t1, t2 = [int(i) for i in input().split()]
h *= 5
t1 *= 5
t2 *= 5
if h < t1: h += 60
if m < t1: m += 60
if s < t1: s += 60
if t2 < t1: t2 += 60
c = (t2 <= h) + (t2 <= m) + (t2 <= s)
ans = "YES" if c == 0 or c == 3 else "NO"
print(ans)

