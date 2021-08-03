def main():
    N, M = [int(i) for i in input().split()]

    pos = 0
    ans = 1

    fib = [1 for _ in range(100002)]
    for i in range(2, 100002):
        fib[i] = fib[i - 1] + fib[i - 2]

    for _ in range(M):

        a = int(input())
        if a == pos:
            ans = 0
            pos = N
            break
        elif a == pos + 1:
            pos = a + 1
        else:
            ans *= fib[(a - 1 - pos)]
            pos = a + 1

    if pos + 1 < N:
        ans *= fib[(N - pos)]

    print((ans % 1_000_000_007))


def __starting_point():
    main()


__starting_point()
