n = int(input())

cnt = [[0] * 10 for i in range(10)]

for i in range(n + 1):
    a = int(str(i)[0])
    b = int(str(i)[-1])
    if a == 0 or b == 0:
        continue
    cnt[a][b] += 1

ans = 0
for i in range(n + 1):
    a = int(str(i)[0])
    b = int(str(i)[-1])
    ans += cnt[b][a]
print(ans)
