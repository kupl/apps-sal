def main():
    N, M = list(map(int, input().split()))  # N must be an odd number

    if N % 2 == 1:
        gen = ((i+1, N-i) for i in range(M))
    else:
        gen = ((i+1, N-i) if 2*i < N/2-1 else (i+1, N-i-1) for i in range(M))

    for s in gen:
        print((*s))


def __starting_point():
    main()

__starting_point()
