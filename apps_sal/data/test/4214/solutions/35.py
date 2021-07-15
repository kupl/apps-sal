import math
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
result = 0

for i in range(N):
    for j in range(N):
        if i != j:
            result += math.sqrt((xy[i][0] - xy[j][0])**2 + (xy[i][1] - xy[j][1])**2)

print((result / N))


