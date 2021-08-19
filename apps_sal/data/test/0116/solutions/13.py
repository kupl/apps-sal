(l1, r1, l2, r2, k) = list(map(int, input().split()))
l = max(l1, l2)
r = min(r1, r2)
ans = max(r - l + 1, 0)
if k >= l and k <= r:
    ans -= 1
print(ans)
