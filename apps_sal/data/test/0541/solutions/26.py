import sys

input = sys.stdin.readline


def main():
    N, M = list(map(int, input().split()))
    AB = [None] * M
    for i in range(M):
        AB[i] = tuple(map(int, input().split()))

    AB.sort(key=lambda x: x[1])

    ans = 0
    prev_x = -1
    for a, b in AB:
        if a <= prev_x < b:
            pass
        else:
            ans += 1
            prev_x = b - 1

    print(ans)


def __starting_point():
    main()

__starting_point()
