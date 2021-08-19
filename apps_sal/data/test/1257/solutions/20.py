(n, k) = map(int, input().split())
data = [[None for i in range(n)] for j in range(n)]
data[0][k - 1] = n ** 2 - n + k
help = 0
answer = data[0][k - 1]
for i in range(1, n):
    data[i][k - 1] = data[i - 1][k - 1] - (n - k + 1)
    answer += data[i][k - 1]
for i in range(n - 1, -1, -1):
    for j in range(k, n):
        data[i][j] = data[i][j - 1] + 1
for i in range(n - 1, -1, -1):
    for j in range(k - 1):
        data[i][j] = help + 1
        help += 1
print(answer)
for i in range(n):
    print(*data[i])
