3


def solve(A, B, C, N):
    if C > A or C > B:
        return -1
    if A + B - C > N:
        return -1
    rest = N - (A + B - C)
    if rest == 0:
        return -1
    return rest


def main():
    (A, B, C, N) = [int(e) for e in input().split(' ')]
    print(solve(A, B, C, N))


def __starting_point():
    main()


__starting_point()
