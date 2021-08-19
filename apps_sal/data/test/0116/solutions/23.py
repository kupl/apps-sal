(l1, r1, l2, r2, k) = list(map(int, input().split()))
'if l1 > l2:\n    r = min(r1,r2)-l1+1\n    if k >= l1 and k <= min(r1,r2):\n        r -= 1\nelif l2 > l1:\n    r = min(r1,r2)-l2+1\n    if k >= l2 and k <= min(r1,r2):\n        r -= 1\nelse:\n    r = min(r1,r2)-l1\n    if k >= l1 and k <= min(r1,r2):\n        r -= 1'
l = max(l1, l2)
r = min(r1, r2)
res = r - l + 1
if k >= l and k <= r:
    res -= 1
print(max(0, res))
