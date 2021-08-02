p, q, l, r = list(map(int, input().split()))
x = [0] * 10000
y = []
cnt = 0
for i in range(p):
    a, b = list(map(int, input().split()))
    for j in range(a, b + 1):
        x[j] = 1
for i in range(q):
    a, b = list(map(int, input().split()))
    y.append((a, b))

for i in range(l, r + 1):
    f = 0
    for j in range(q):
        if not f:
            for k in range(y[j][0] + i, y[j][1] + i + 1):
                if x[k]:
                    f = 1
                    break
        else:
            break
    cnt += f
print(cnt)
