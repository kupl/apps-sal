def ok(x):
    need = 0
    for i in range(n):
        tmp = a[i] * x - b[i]
        if tmp > 0:
            need += tmp
    return need <= k
n, k = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
lo, hi = 0, 2 * 10 ** 9
while lo <= hi:
    mid = (lo + hi) >> 1
    if ok(mid):
        lo = mid + 1
    else:
        hi = mid - 1
print(hi)

