import sys
3
sys.setrecursionlimit(10 ** 9)


def bscheck(n, l, v1, v2, k, t):
    while True:
        if k > n:
            k = n
        if n == 0:
            return True
        if l / v2 > t:
            return False
        tx = (l - v1 * t) / (v2 - v1)
        ty = (tx * v2 - tx * v1) / (v1 + v2)
        _n = n - k
        _l = l - tx * v1 - ty * v1
        _t = t - tx - ty
        n = _n
        l = _l
        t = _t


(n, l, v1, v2, k) = list(map(int, input().split()))
(lt, rt) = (0, 1791791791)
for i in range(100):
    mid = (lt + rt) / 2
    if bscheck(n, l, v1, v2, k, mid):
        rt = mid
    else:
        lt = mid
print(rt)
