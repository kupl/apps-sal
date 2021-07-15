import sys

input = sys.stdin.readline


def main():
    N, T = [int(x) for x in input().split()]
    CT = [[int(x) for x in input().split()] for _ in range(N)]

    ans = float("inf")
    for c, t in CT:
        if t <= T:
            ans = min(ans, c)

    if ans == float("inf"):
        print("TLE")
    else:
        print(ans)


def __starting_point():
    main()

__starting_point()
