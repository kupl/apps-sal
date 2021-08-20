def manhattan(n, x, y):
    x2 = [0] * n
    y2 = [0] * n
    for i in range(n):
        x2[i] = x[i] - y[i]
        y2[i] = x[i] + y[i]
    print(max(max(x2) - min(x2), max(y2) - min(y2)))


n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    (x[i], y[i]) = list(map(int, input().split()))
manhattan(n, x, y)
