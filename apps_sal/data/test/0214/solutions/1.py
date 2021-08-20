3


def o(c):
    return c == '0'


def solve(A, B, N):
    A += 'XXX'
    B += 'XXX'
    i = 0
    c = 0
    while i < N:
        if o(A[i]) and o(A[i + 1]) and o(A[i + 2]) and o(B[i]) and o(B[i + 1]) and o(B[i + 2]):
            c += 2
            i += 3
            continue
        x = len([x for x in [o(A[i]), o(A[i + 1]), o(B[i]), o(B[i + 1])] if x])
        if x >= 3:
            c += 1
            i += 2
            continue
        i += 1
    return c


def main():
    A = input()
    B = input()
    N = len(A)
    assert len(B) == N
    print(solve(A, B, N))


def __starting_point():
    main()


__starting_point()
