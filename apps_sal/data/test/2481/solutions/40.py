h, w = list(map(int, input().split()))
c = [list(map(int, input().split())) for _ in range(10)]
num = [0] * 10
for _ in range(h):
    a = list(map(int, input().split()))
    for i in a:
        if i == -1:
            continue
        num[i] += 1
for i in range(10):
    for j in range(10):
        for k in range(10):
            c[j][k] = min(c[j][k], c[j][i] + c[i][k])
print((sum(num[x] * c[x][1] for x in range(10))))
