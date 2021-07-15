from bisect import bisect_left, bisect_right
from itertools import accumulate

def solve():
    N, M = list(map(int, input().split()))
    As = list(map(int, input().split()))

    As.sort()

    def isOK(x):
        num = 0
        for k, A in enumerate(As, start=1):
            i = bisect_left(As, x-A)
            num += N-i
            if num >= M:
                return True
            elif num + (N-k)*N < M:
                return False
        return num >= M

    ng, ok = 2*10**5+1, 0
    while abs(ok-ng) > 1:
        mid = (ng+ok) // 2
        if isOK(mid):
            ok = mid
        else:
            ng = mid
#    print('ok:', ok)

    score = 0
    num = 0
    accAs = list(accumulate([0]+As))
    for A in As:
        i = bisect_right(As, ok-A)
        score += A*(N-i) + accAs[N] - accAs[i]
        num += N-i
#    print('score:', score, '/ num:', num)

    ans = score + ok*(M-num)
    print(ans)


solve()

