N = int(input())
bucket = [[0] * 10 for _ in range(10)]
for n in range(1, N + 1):
    n = str(n)
    bucket[int(n[0])][int(n[-1])] += 1
ans = 0
for i in range(10):
    for j in range(10):
        ans += bucket[i][j] * bucket[j][i]
print(ans)
