import sys

input = sys.stdin.readline


def main():
    M, K = list(map(int, input().split()))

    if K >= 2 ** M:
        print((-1))
        return

    if M == 1:
        if K == 0:
            print((0, 0, 1, 1))
        else:
            print((-1))
        return

    A = list(range(2 ** M))
    B = list(reversed(list(range(2 ** M))))
    A.remove(K)
    B.remove(K)

    ans = A + [K] + B + [K]
    print((" ".join(map(str, ans))))


def __starting_point():
    main()


__starting_point()
