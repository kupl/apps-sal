def main():
    n, m, k = list(map(int, input().split()))
    aa, t = list(map(int, input().split())), n * m * k
    aa.reverse()
    for _ in range(n):
        for a in map(int, input().split()):
            i = aa.index(a)
            t -= i
            del aa[i]
            aa.append(a)
    print(t)


def __starting_point():
    main()

__starting_point()
