import sys
pin = sys.stdin.readline


def main():
    N = int(pin())
    L = list(map(int, pin().split()))
    L.sort()
    ans = 0
    for i in range(0, 2 * N, 2):
        ans += L[i]
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
