N = int(input())
num = [[0] * 10 for i in range(10)]
for i in range(1, N + 1):
    top = int(str(i)[0])
    end = int(str(i)[-1])
    num[top][end] += 1
count = 0
for i in range(10):
    for j in range(10):
        count += num[i][j] * num[j][i]
print(count)
