n, m = list(map(int, input().split()))
p_y = []
for i in range(m):
    p, y = list(map(int, input().split()))
    p_y.append([p, y, i])

p_y.sort()
# print(p_y)

res = [0] * m
order = 0
for i in range(m):
    ken, _, index = p_y[i]
    if ken != p_y[i - 1][0] and i > 0:
        order = 1
    else:
        order += 1
    res[index] = [ken, order]


# print(res)

for i in range(m):
    ken = str(res[i][0]).zfill(6)
    order = str(res[i][1]).zfill(6)
    print((ken + order))

