
def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    S = A[0] + A[1]

    xor = 0
    for a in A[2:]:
        xor ^= a

    S -= xor
    if S % 2 == 1:
        return print(-1)

    S //= 2
    if (S & xor) != 0 or S > A[0]:
        return print(-1)

    b = S
    for i in range(41, -1, -1):
        if xor >> i & 1 == 1:
            if b + (1 << i) <= A[0]:
                b += 1 << i

    if b == 0:
        print(-1)
    else:
        print(A[0] - b)


def __starting_point():
    resolve()


__starting_point()
