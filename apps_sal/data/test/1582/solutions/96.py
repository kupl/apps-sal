N = int(input())

ans = 0
cnt = [[0] * 10 for i in range(10)]

for i in range(1, N + 1):
    cnt[int(str(i)[0])][int(str(i)[-1])] += 1

for i in range(1, N + 1):
    ans += cnt[int(str(i)[-1])][int(str(i)[0])]

print(ans)
