N, X, Y = map(int, input().split())
A = [0] * (N - 1)
for i in range(1, N):
    for j in range(i + 1, N + 1):
        A[min(j - i, abs(X - i) + 1 + abs(j - Y), abs(Y - i) + 1 + abs(j - X)) - 1] += 1
for a in A:
    print(a)
