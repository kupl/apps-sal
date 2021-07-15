l1, r1, l2, r2, k = map(int, input().split())
ans = max(0, min(r1, r2) - max(l1, l2) + 1)
if max(l1, l2) <= k <= min(r1, r2):
    ans = max(ans - 1, 0)
print(ans)
