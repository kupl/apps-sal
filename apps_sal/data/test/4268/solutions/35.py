import math
n, d = list(map(int, input().split()))
x = []
for _ in range(n):
    l = list(map(int, input().split()))
    x.append(l)
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        tmp = 0
        for k in range(d):
            tmp += (x[i][k] - x[j][k])**2
        if math.sqrt(tmp) == int(math.sqrt(tmp)):
            cnt += 1
print(cnt)
