(n, k) = map(int, input().split())
a = list(map(int, input().split()))
ng = 0
ok = max(a)
while ng + 1 != ok:
    mid = (ng + ok) // 2
    ans = 0
    for aa in a:
        if aa % mid == 0:
            ans += aa // mid - 1
        else:
            ans += aa // mid
    if ans <= k:
        ok = mid
    else:
        ng = mid
print(ok)
