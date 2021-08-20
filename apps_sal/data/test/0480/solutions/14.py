(s, x1, x2) = map(int, input().split())
(t1, t2) = map(int, input().split())
(p, d) = map(int, input().split())
ig = abs(x2 - x1) * t2
tr = ig
if d < 0:
    if x2 < x1:
        if x1 <= p:
            tr = (p - x2) * t1
        else:
            tr = (p + s + (s - x2)) * t1
    else:
        tr = (p + x2) * t1
elif x1 < x2:
    if p <= x1:
        tr = (x2 - p) * t1
    else:
        tr = (s - p + s + x2) * t1
else:
    tr = (s - p + (s - x2)) * t1
ans = min(ig, tr)
print(ans)
