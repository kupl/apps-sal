(l1, r1, l2, r2, k) = map(int, input().split())
l = l1
if l2 > l:
    l = l2
r = r1
if r2 < r:
    r = r2
if r < l:
    print(0)
elif l <= k <= r:
    print(r - l)
else:
    print(r - l + 1)
