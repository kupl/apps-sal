import itertools

N = int(input())
L = []

for i in range(N):
    x, y = map(int, input().split())
    L.append([x, y])

cnt = 0
total = 0
for v in itertools.permutations(L):
    for i in range(N - 1):
        x_1 = v[i][0]
        y_1 = v[i][1]
        x_2 = v[i + 1][0]
        y_2 = v[i + 1][1]
        total += ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5
    cnt += 1

print(total / cnt)
