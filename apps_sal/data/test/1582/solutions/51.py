n = int(input())
count = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(10)]
for i in range(1, n + 1):
    count[int(list(str(i))[0]) - 1][int(list(str(i))[-1]) - 1] += 1
ans = 0
for j in range(10):
    for k in range(10):
        ans += (count[j][k] * count[k][j])
print(ans)
