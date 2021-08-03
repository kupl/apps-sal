N = int(input())
counter = [[0 for _ in range(10)] for _ in range(10)]
for k in range(1, N + 1):
    counter[k % 10][int(str(k)[0])] += 1
ans = 0
for k in range(1, 10):
    for j in range(1, 10):
        ans += counter[k][j] * counter[j][k]
print(ans)
