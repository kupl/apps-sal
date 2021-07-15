import sys

inf = 1 << 30

def solve():
    n, k = map(int, input().split())

    # list divisors of n
    a = []
    b = []

    for d in range(1, n + 1):
        if d*d > n:
            break
        if n % d != 0:
            continue

        a.append(d)
        b.append(n // d)

    b.reverse()

    if a[-1] == b[0]:
        divs = a + b[1:]
    else:
        divs = a + b

    # main process

    d_m = -1
    need = k * (k + 1) // 2

    for d in divs:
        q = n // d

        if q >= need:
            d_m = d
        else:
            break

    if d_m == -1:
        print(-1)
    else:
        ans = [0]*k

        for i in range(k - 1):
            ans[i] = (i + 1) * d_m

        ans[-1] = n - d_m * k * (k - 1) // 2

        print(*ans)

def __starting_point():
    solve()
__starting_point()
