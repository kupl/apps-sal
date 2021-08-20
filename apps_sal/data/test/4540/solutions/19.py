import sys
stdin = sys.stdin


def ns():
    return stdin.readline().rstrip()


def ni():
    return int(stdin.readline().rstrip())


def nm():
    return list(map(int, stdin.readline().split()))


def nl():
    return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    A = nl()
    total = sum([abs(A[i + 1] - A[i]) for i in range(n - 1)])
    for i in range(n):
        if i == 0:
            start = abs(A[1])
            end = abs(A[-1])
            print(total - abs(A[1] - A[0]) + start + end)
        elif i == n - 1:
            start = abs(A[0])
            end = abs(A[-2])
            print(total - abs(A[-2] - A[-1]) + start + end)
        else:
            start = abs(A[0])
            end = abs(A[-1])
            print(total - abs(A[i - 1] - A[i]) - abs(A[i] - A[i + 1]) + abs(A[i + 1] - A[i - 1]) + start + end)


def __starting_point():
    main()


__starting_point()
