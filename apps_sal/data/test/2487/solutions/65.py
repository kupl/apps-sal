import sys


def read():
    return sys.stdin.readline()


def main():
    n = int(read())
    d = [0] * n
    present = [[] for i in range(n)]
    for i in range(n - 1):
        u, v = sorted([int(x) - 1 for x in read().split()])
        d[v] += 1
        present[u].append(v)
    ans, cur = 0, 0
    for v in range(n):
        cur += (n - v) * d[v]
    for L in range(n):
        ans += (L + 1) * (L + 2) // 2 - cur
        for v in present[L]:
            cur -= (n - v)
    print(ans)


def __starting_point():
    main()


__starting_point()
