n, k = map(int, input().split())
k -= 1
answer = [[0] * n for i in range(n)]
cur = 1
for i in range(n):
    for j in range(k):
        answer[i][j] = cur
        cur += 1
for i in range(n):
    for j in range(k, n):
        answer[i][j] = cur
        cur += 1
summa = 0
for i in range(n):
    summa += answer[i][k]
print(summa)
for i in range(n):
    print(*answer[i])
