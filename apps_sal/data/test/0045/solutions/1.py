import sys

inf = 1 << 30

def solve():
    n, k = map(int, input().split())

    lim = k * (k + 1) // 2

    if n < lim:
        print(-1)
        return

    d_max = 1

    for d in range(1, n + 1):
        if d*d > n:
            break
        if n % d != 0:
            continue

        q = n // d

        if d >= lim:
            d_max = q
            break
        elif q >= lim:
            d_max = d
        else:
            break

    ans = []
    j = 1

    for i in range(k - 1):
        ans.append(d_max * j)
        j += 1

    ans.append(n - sum(ans))

    print(*ans)

def __starting_point():
    solve()
__starting_point()
