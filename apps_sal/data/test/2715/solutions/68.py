from sys import stdin


def main():
    readline = stdin.readline
    K = int(readline())

    N = 50
    M = K // N
    L = K % N
    A = range(N)
    A = list(map(lambda x: x + M, A))
    for i in range(L):
        A[i] += N + 1
        A = list(map(lambda x: x - 1, A))

    print(N)
    print(*A)


def __starting_point():
    main()


__starting_point()
