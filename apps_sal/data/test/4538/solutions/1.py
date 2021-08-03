N, D = map(int, input().split())

xy = [list(map(int, input().split())) for i in range(N)]

cnt = 0

for x, y in xy:
    if (x**2 + y**2)**(1 / 2) <= D:
        cnt += 1

print(cnt)
