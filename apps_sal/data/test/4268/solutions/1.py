import math

N, D = map(int, input().split())

X = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(N):
        if i < j:
            distance = 0
            for k in range(D):
                distance += (X[i][k] - X[j][k]) ** 2
            distance = math.sqrt(distance)
            if distance == int(distance):
                result += 1

print(result)
