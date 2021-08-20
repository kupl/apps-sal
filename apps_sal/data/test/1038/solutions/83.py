import sys
input = sys.stdin.readline


def g(N):
    if N == -1:
        return 0
    r = N % 4
    if r == 0:
        return N
    elif r == 1:
        return 1
    elif r == 2:
        return N + 1
    else:
        return 0


def main():
    (A, B) = list(map(int, input().split()))
    ans = g(A - 1) ^ g(B)
    print(ans)


def __starting_point():
    main()


__starting_point()
