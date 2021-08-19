(l1, r1, l2, r2, k) = map(int, input().split())
lmax = max(l1, l2)
rmin = min(r1, r2)
if lmax > rmin:
    print(0)
else:
    ans = rmin - lmax + 1
    if k >= lmax and k <= rmin:
        ans -= 1
    print(ans)
