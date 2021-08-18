n = int(input())

cnt = [[0 for i in range(10)] for j in range(10)]

for k in range(n + 1):
    head = int(str(k)[0])
    foot = int(str(k)[-1])
    cnt[head][foot] += 1

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += cnt[i][j] * cnt[j][i]

print(ans)
