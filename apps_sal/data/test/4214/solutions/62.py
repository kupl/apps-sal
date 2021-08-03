N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
d = 0
for i in range(N):
    for j in range(N):
        d += ((city[i][0] - city[j][0])**2 + (city[i][1] - city[j][1])**2)**0.5
print(d / N)
