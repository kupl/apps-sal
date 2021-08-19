(A, B) = map(int, input().split())


def f(N):
    if N % 2 == 1:
        return (N + 1) // 2 % 2
    else:
        return N // 2 % 2 ^ N


print(f(A - 1) ^ f(B))
