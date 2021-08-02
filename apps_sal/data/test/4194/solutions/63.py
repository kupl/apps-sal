N, M = list(map(int, input().split()))
A = list(map(int, input().split()))


def answer(N: int, M: int, A: list) -> int:
    A = sum(A)
    if N < A:
        return -1
    else:
        return N - A


print((answer(N, M, A)))
