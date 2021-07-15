N, K, M = list(map(int, input().split()))
A = list(map(int, input().split()))

def answer(N: int, K: int, M: int, A: list) -> int:
    A = sum(A)
    if max(0, M * N - A) > K:
        return -1
    else:
        return(max(0, M * N - A))

print((answer(N, K, M, A)))


