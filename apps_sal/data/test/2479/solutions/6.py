from collections import deque
from bisect import bisect_left


def main():
    (N, Q) = list(map(int, input().split()))
    Query = [tuple(map(int, input().split())) for _ in range(Q)]
    LX = 1
    X = deque([N])
    VX = deque([N])
    LY = 1
    Y = deque([N])
    VY = deque([N])
    mx = N
    my = N
    ans = 0
    for (i, x) in Query:
        if i == 1:
            if x < my:
                ans += mx - 2
                X.appendleft(x)
                VX.appendleft(mx)
                my = x
            else:
                ans += VX[bisect_left(X, x) - 1] - 2
        elif x < mx:
            ans += my - 2
            Y.appendleft(x)
            VY.appendleft(my)
            mx = x
        else:
            ans += VY[bisect_left(Y, x) - 1] - 2
    print((N - 2) ** 2 - ans)


def __starting_point():
    main()


__starting_point()
