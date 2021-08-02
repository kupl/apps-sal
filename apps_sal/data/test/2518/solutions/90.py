import sys

input = sys.stdin.readline


def main():
    n, a, b = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()

    l, r = -1, h[-1] + 1
    while r - l > 1:
        key = (r + l) // 2
        count = 0
        for i in range(n):
            if h[i] <= key * b:
                continue
            else:
                count += (h[i] - key * b - 1) // (a - b) + 1
        if count <= key:
            r = key
        else:
            l = key
    print(r)


def __starting_point():
    main()


__starting_point()
