import sys


def solve():
    input = sys.stdin.readline
    A, B, C, D = map(int, input().split())
    ans = 0
    fib = [0] * (D + 1)
    fib[1] = 1
    for i in range(2, D + 1):
        if i <= C - B + 1:
            fib[i] = fib[i - 1] + i
        else:
            fib[i] = fib[i - 1] + (C - B + 1)
    for z in range(C, D + 1):
        if B + C <= z:
            continue
        else:
            xlow = z - C + 1
            pN = B - xlow + 1
            psubN = A - xlow
            if xlow >= A:
                ans += fib[pN]
            else:
                ans += fib[pN] - fib[psubN]

    print(ans)

    return 0


def __starting_point():
    solve()


__starting_point()
