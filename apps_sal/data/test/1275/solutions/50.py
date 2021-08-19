import sys
sys.setrecursionlimit(10 ** 9)


def read():
    return sys.stdin.readline()


def read_ints():
    return list(map(int, read().split()))


def read_intgrid(h):
    return list((list(map(int, read().split())) for i in range(h)))


def read_strgrid(h):
    return list((list(read()) for i in range(h)))


def main():
    (n, k) = map(int, read().split())
    '\n    半分全列挙する。n以下の数で作れる数rの組み合わせを考えるクロス表作ればわかる。\n    r==n+1の時、n個\n    r<n+1の時、r-1\n    r>n+1の時、2n-r+!\n    '
    k = abs(k)
    combs = [0] * (n * 2 + 1)
    for i in range(1, n * 2 + 1):
        if i == n + 1:
            combs[i] = n
        elif i < n + 1:
            combs[i] = i - 1
        elif i > n + 1:
            combs[i] = 2 * n - i + 1
    cnt = 0
    for i in range(1, n * 2 + 1):
        cnt += combs[i] * combs[max(0, i - k)]
    print(cnt)
    return None


def __starting_point():
    main()


__starting_point()
