from math import ceil
(N, K) = list(map(int, input().split()))
A = list(map(int, input().split()))


def f(x):
    cnt = 0
    for a in A:
        cnt += ceil(a / x) - 1
    return True if cnt <= K else False


(OK, NG) = (10 ** 9, 0)
while OK - NG > 1:
    mid = (OK + NG) // 2
    if f(mid):
        OK = mid
    else:
        NG = mid
print(OK)
