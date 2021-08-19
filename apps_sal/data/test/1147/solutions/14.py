from bisect import bisect_left


def R():
    return list(map(int, input().split()))


(n, x, k) = R()
a = sorted(R())
print(sum((bisect_left(a, l + x) - bisect_left(a, max(u, l)) for (u, l) in ((u, ((u - 1) // x + k) * x) for u in a))))
