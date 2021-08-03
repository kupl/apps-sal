N = int(input())
A = [0] + [int(X) for X in input().split()] + [0]
Cost = sum(abs(A[T + 1] - A[T]) for T in range(N + 1))
for T in range(1, N + 1):
    Cut = Cost + abs(A[T + 1] - A[T - 1]) - abs(A[T] - A[T - 1]) - abs(A[T + 1] - A[T])
    print(Cut)
