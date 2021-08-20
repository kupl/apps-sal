from math import sqrt
s = input().split()
s = [int(s) for s in s]
(r, x, y, x1, y1) = (s[0], s[1], s[2], s[3], s[4])
d = sqrt((x - x1) ** 2 + (y - y1) ** 2)
ans = d // (r * 2)
if d > ans * r * 2:
    ans += 1
print(int(ans))
