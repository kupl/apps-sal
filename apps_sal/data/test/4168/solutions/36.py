import sys

input = sys.stdin.readline


def main():
    N = int(input())

    if N == 0:
        ans = "0"
    else:
        ans = ""
        while N != 0:
            q, r = divmod(N, -2)
            if r == 0:
                ans = "".join(["0", ans])
            else:
                ans = "".join(["1", ans])
            r = r + 2 if r < 0 else r
            N = (N - r) // -2

    print(ans)


def __starting_point():
    main()

__starting_point()
