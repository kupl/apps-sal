def sigma(k):
    return k * (k + 1) // 2


n = int(input())
ub = 10 ** 18
lb = 1
while ub - lb > 1:
    mid = (ub + lb) // 2
    if sigma(mid) <= n + 1:
        lb = mid
    else:
        ub = mid
print(n - lb + 1)
