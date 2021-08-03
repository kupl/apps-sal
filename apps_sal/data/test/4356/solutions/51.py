import numpy


def main():
    n, m = map(int, input().split())
    a = numpy.array([list(input()) for _ in range(n)])
    b = numpy.array([list(input()) for _ in range(m)])
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            if numpy.all(a[i: i + m, j: j + m] == b):
                print("Yes")
                return
    print("No")


def __starting_point():
    main()


__starting_point()
