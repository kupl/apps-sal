def main():
    n, m, k = list(map(int, input().split()))
    aa, t = list(map(int, input().split())), n * m * k
    aa.reverse()
    u, v, w = aa.index, aa.remove, aa.append
    for _ in range(n):
        for a in map(int, input().split()):
            t -= u(a)
            v(a)
            w(a)
    print(t)


def __starting_point():
    main()

__starting_point()
