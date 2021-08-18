import sys


def solve(M: int, K: int):
    if K >= (1 << M):
        print(-1)
        return
    if M == 1:
        if K == 0:
            print(0, 0, 1, 1)
        else:
            print(-1)
        return
    for i in range(1 << M):
        if i != K:
            print(i, end=" ")
    print(K, end=" ")
    for i in reversed(range(1 << M)):
        if i != K:
            print(i, end=" ")
    print(K)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    M = int(next(tokens))
    K = int(next(tokens))
    solve(M, K)


def __starting_point():
    main()


__starting_point()
