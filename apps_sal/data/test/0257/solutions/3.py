def main():
    import sys
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline
    from math import hypot
    from collections import deque

    N, K = map(int, input().split())
    XYC = [tuple(map(int, input().split())) for _ in range(N)]

    dq = deque([(0, 0, 1000.0)])

    ans = 10**18
    while dq:
        X, Y, r = dq.popleft()
        c_hypot = [c * hypot(max(abs(X - x) - r, 0), max(abs(Y - y) - r, 0)) for x, y, c in XYC]
        c_hypot.sort()
        if ans * 0.9999995 > c_hypot[K-1]:
            c_hypot = [c * hypot(X - x, Y - y) for x, y, c in XYC]
            c_hypot.sort()
            if c_hypot[K-1] < ans:
                ans = c_hypot[K-1]

            r /= 2
            dq += [
                (X + r, Y + r, r),
                (X - r, Y + r, r),
                (X + r, Y - r, r),
                (X - r, Y - r, r),
            ]
    print(ans)

main()
