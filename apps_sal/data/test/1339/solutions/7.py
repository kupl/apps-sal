(vl, vr, vi, maxr) = (1000000001, 0, 0, 0)
for i in range(1, int(input()) + 1):
    (l, r) = (int(x) for x in input().split())
    if l < vl or (l == vl and r > vr):
        (vl, vr, vi) = (l, r, i)
    maxr = max(maxr, r)
print(vi if vr >= maxr else -1)
