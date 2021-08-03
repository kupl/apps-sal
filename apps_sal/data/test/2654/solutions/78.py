def main():
    n = int(input())
    a, b = [None] * n, [None] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    if n & 1:
        print(b[n // 2] - a[n // 2] + 1)
    else:
        print(b[n // 2 - 1] + b[n // 2] - a[n // 2 - 1] - a[n // 2] + 1)


def __starting_point():
    main()


__starting_point()
