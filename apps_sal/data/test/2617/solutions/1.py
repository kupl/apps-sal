import sys
stdin = sys.stdin


def ns():
    return stdin.readline().rstrip()


def ni():
    return int(stdin.readline().rstrip())


def nm():
    return list(map(int, stdin.readline().split()))


def nl():
    return list(map(int, stdin.readline().split()))


def solve():
    n = ni()
    da = n.bit_length() - 1
    print(da)
    n -= da + 1
    f = [0] * da
    mx = 1
    for i in range(da):
        gr = min(mx, n // (da - i))
        f[i] = gr
        mx += gr
        n -= (da - i) * gr
    print(*f)


t = ni()
for _ in range(t):
    solve()
