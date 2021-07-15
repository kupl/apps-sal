N, M = map(int, input().split())
drinks = []

for i in range(N):
    drinks.append(tuple(map(int, input().split())))

drinks.sort()

cnt = 0
res = 0
for i in range(N):
    res += (min(cnt + drinks[i][1], M) - cnt) * drinks[i][0]
    cnt += drinks[i][1]

    if cnt >= M:
        break

print(res)
