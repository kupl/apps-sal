n = int(input())
a = list(map(int, input().split()))
b = [0] * (n + 1)
for i in range(n):
    b[i + 1] = b[i] + a[i]
x = [[0, 0] for _ in range(n - 3)]
j = 1
for i in range(2, n - 1):
    while True:
        if i == j + 1:
            x[i - 2][0] = b[j]
            break
        if abs(b[i] - 2 * b[j]) > abs(b[i] - 2 * b[j + 1]):
            j += 1
        else:
            x[i - 2][0] = b[j]
            break
j = n - 1
for i in range(n - 2, 1, -1):
    while True:
        if i == j - 1:
            x[i - 2][1] = b[j]
            break
        if abs(b[n] + b[i] - 2 * b[j]) > abs(b[n] + b[i] - 2 * b[j - 1]):
            j -= 1
        else:
            x[i - 2][1] = b[j]
            break
ans = 1145141919810
for i in range(n - 3):
    s = [x[i][0], b[i + 2] - x[i][0], x[i][1] - b[i + 2], b[n] - x[i][1]]
    ans = min(ans, max(s) - min(s))
print(ans)
