n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort()


def check(x):
    for i in range(n):
        if i + k - 1 >= n:
            continue
        if h[i + k - 1] - h[i] <= x:
            return True
    return False


hmax, hmin = max(h), min(h)
fv, tv = -1, (hmax - hmin)
while tv - fv > 1:
    mid = (tv + fv) // 2
    if check(mid):
        tv = mid
    else:
        fv = mid
print(tv)
