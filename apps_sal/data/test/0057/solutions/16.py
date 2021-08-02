n = int(input())
p = [0] * n
for i in range(n):
    p[i] = tuple(map(int, input().split()))

if n == 4:
    for i in range(1, 4):
        if p[0][0] != p[i][0] and p[0][1] != p[i][1]:
            res = abs(p[0][0] - p[i][0]) * abs(p[0][1] - p[i][1])
elif n == 3:
    for i in range(1, 3):
        if p[0][0] != p[i][0] and p[0][1] != p[i][1]:
            res = abs(p[0][0] - p[i][0]) * abs(p[0][1] - p[i][1])
    for i in [0, 2]:
        if p[1][0] != p[i][0] and p[1][1] != p[i][1]:
            res = abs(p[1][0] - p[i][0]) * abs(p[1][1] - p[i][1])
elif n == 2:
    if p[0][0] != p[1][0] and p[0][1] != p[1][1]:
        res = abs(p[0][0] - p[1][0]) * abs(p[0][1] - p[1][1])
    else: res = -1

else:
    res = -1

print(res)
