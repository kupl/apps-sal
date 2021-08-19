def check(mid):
    need = 0
    for i in range(mid):
        if mon[n - mid + i] < pri[i]:
            need += pri[i] - mon[n - mid + i]
    return need <= a


(n, m, a) = list(map(int, input().split()))
mon = sorted(map(int, input().split()))
pri = sorted(map(int, input().split()))
l = 0
r = min(n, m)
while l <= r:
    mid = l + (r - l) // 2
    if check(mid):
        l = mid + 1
    else:
        r = mid - 1
print(r, max(0, sum(pri[:r]) - a))
