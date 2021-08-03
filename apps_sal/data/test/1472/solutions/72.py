N, X, Y = list(map(int, input().split()))

d = [0] * N
for i in range(1, N):
    for j in range(i + 1, N + 1):
        if j <= X:
            a = j - i
        elif i <= X and j >= Y:
            a = (X - i) + (j - Y) + 1
        else:
            a = min(j - i, abs(X - i) + 1 + abs(Y - j))

        d[a] += 1
for ans in d[1:]:
    print(ans)
