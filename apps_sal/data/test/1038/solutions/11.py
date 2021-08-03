A, B = map(int, input().split())


def sumXOR(N):
    rm = N % 4
    if rm == 0:
        k = N
    elif rm == 1:
        k = 1
    elif rm == 2:
        k = N + 1
    else:
        k = 0
    return k


print(sumXOR(A - 1) ^ sumXOR(B))
