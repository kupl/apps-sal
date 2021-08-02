def main():
    import sys
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    n, res, j = int(input()), [], 0
    cc, f = sorted(map(int, input().split())), res.append
    for i, c in enumerate(cc):
        while cc[j] * 2 < c:
            j += 1
        f(i - j)
    print(n - max(res) - 1)


def __starting_point():
    main()


__starting_point()
