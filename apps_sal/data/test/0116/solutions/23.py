
l1, r1, l2, r2, k = list(map(int, input().split()))

"""if l1 > l2:
    r = min(r1,r2)-l1+1
    if k >= l1 and k <= min(r1,r2):
        r -= 1
elif l2 > l1:
    r = min(r1,r2)-l2+1
    if k >= l2 and k <= min(r1,r2):
        r -= 1
else:
    r = min(r1,r2)-l1
    if k >= l1 and k <= min(r1,r2):
        r -= 1"""
l = max(l1, l2)
r = min(r1, r2)
res = r - l + 1
if k >= l and k <= r:
    res -= 1
print(max(0, res))
