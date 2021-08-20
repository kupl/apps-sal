(l1, r1, l2, r2, k) = map(int, input().split())
l = max(l1, l2)
r = min(r1, r2)
count = max(r - l + 1, 0)
if l <= k <= r:
    count -= 1
print(count)
