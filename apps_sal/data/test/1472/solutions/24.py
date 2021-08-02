N, X, Y = map(int, input().split())
lst = [0 for i in range(N - 1)]
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        k = min(abs(j - i), abs(X - i) + abs(Y - j) + 1)
        lst[k - 1] += 1
for i in lst:
    print(i)
