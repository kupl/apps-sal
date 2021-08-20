n = int(input())
m = list((tuple(map(int, input().split())) for _ in range(n)))
mid = {}
pall = 0
for i in range(n):
    for j in range(i + 1, n):
        if ((m[i][0] + m[j][0]) / 2, (m[i][1] + m[j][1]) / 2) in mid:
            pall += mid[(m[i][0] + m[j][0]) / 2, (m[i][1] + m[j][1]) / 2]
            mid[(m[i][0] + m[j][0]) / 2, (m[i][1] + m[j][1]) / 2] += 1
        else:
            mid[(m[i][0] + m[j][0]) / 2, (m[i][1] + m[j][1]) / 2] = 1
print(pall)
