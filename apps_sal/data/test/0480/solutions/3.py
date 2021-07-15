s, x1, x2 = map(int, input().split())
t1, t2 = map(int, input().split())
p, d = map(int, input().split())
ans = abs(x1 - x2) * t2
if x1 == x2:
    print(0)
elif x1 < x2:
    if (d == 1 and p <= x1) or p == 0:
        ans = min(ans, abs(x2 - p) * t1)
    elif d == -1 or p == s:
        ans = min(ans, (p + x2) * t1)
    elif d == 1 and p > x1:
        ans = min(ans, (s - p + s + x2) * t1)
else:
    if (d == -1 and p >= x1) or p == s:
        ans = min(ans, abs(p - x2) * t1)
    elif d == 1 or p == 0:
        ans = min(ans, (s - p + s - x2) * t1)
    elif d == -1 and p < x1:
        ans = min(ans, (p + s + s - x2) * t1)
print(ans)
