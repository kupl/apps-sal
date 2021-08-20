import sys


def main():
    input = sys.stdin.readline()
    (n, k, m, t) = [int(j) for j in input.split()]
    for i in range(t):
        input = sys.stdin.readline()
        (d, c) = [int(j) for j in input.split()]
        if d == 0:
            if c < k:
                n -= c
                k -= c
            else:
                n = c
        else:
            if c <= k:
                k += 1
            n += 1
        print(n, k)


def __starting_point():
    main()


__starting_point()
