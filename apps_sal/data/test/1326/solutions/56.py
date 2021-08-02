import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    n = int(input())
    if n == 1:
        print(1)
        return
    r = 0
    for i1 in range(1, n + 1):
        y = n // i1
        r += y * (y + 1) // 2 * i1
    print(r)


def __starting_point():
    main()


__starting_point()
