3

def solve(N, M, A):
    A = [0] + A + [M]

    D = [A[i + 1] - A[i] for i in range(N + 1)]
    LD = len(D)

    evensum = 0
    oddsum = 0
    for i in range(LD):
        if i % 2 == 0:
            evensum += D[i]
        else:
            oddsum += D[i]

    best = evensum
    accum = 0
    for i in range(LD):
        d = D[i]

        if i % 2 == 0:
            evensum -= d
            if d > 1:
                best = max(best, accum + d - 1 + oddsum)
            accum += d
        else:
            oddsum -= d
            if d > 1:
                best = max(best, accum + d - 1 + oddsum)

    return best


def main():
    N, M = [int(e) for e in input().split(' ')]
    A = [int(e) for e in input().split(' ')]
    assert len(A) == N
    print(solve(N, M, A))


def __starting_point():
    main()

__starting_point()
