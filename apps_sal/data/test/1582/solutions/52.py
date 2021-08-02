N = int(input())

cnt = [[0] * 10 for _ in range(10)]

for i in range(1, N + 1):
    x = i
    while x >= 10:
        x //= 10
    cnt[x][i % 10] += 1

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += cnt[i][j] * cnt[j][i]

print(ans)
