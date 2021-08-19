3


def time1(n, t, k):
    return (n + k - 1) // k * t


def num2(T, t, k, d):
    return T // t * k + max(0, (T - d) // t) * k


def time2(n, t, k, d):
    (l, r) = (0, 10 ** 18)
    while l < r - 1:
        mid = (l + r) // 2
        if num2(mid, t, k, d) < n:
            l = mid
        else:
            r = mid
    return r


(n, t, k, d) = list(map(int, input().split()))
if time1(n, t, k) <= time2(n, t, k, d):
    print('NO')
else:
    print('YES')
