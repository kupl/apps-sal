def check(x, A, K):
    import math
    sumA = 0
    for a in A:
        if a > x:
            sumA += math.ceil(a / x) - 1
    if sumA <= K:
        return True
    else:
        return False


def resolve():
    _, K = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]

    ok = max(A)  # maxVal when minimize
    ng = -1  # maxVal when maximize
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if mid > 0 and check(mid, A, K):
            ok = mid
        else:
            ng = mid
    print(ok)


resolve()
