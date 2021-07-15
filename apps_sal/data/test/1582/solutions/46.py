n = int(input())
num = [[0 for _ in range(10)] for _ in range(10)]
for i in range(1, n + 1):
    num[int(str(i)[0])][int(str(i)[-1])] += 1
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += num[i][j] * num[j][i]
print(ans)
