n, m = list(map(int, input().split()))

n = n - 1
et = []
for i in range(m):
    et.append(tuple(map(lambda x: int(x) - 1, input().split())))
et.sort()
res = -1
if n == 0:
    res = 1
elif len(et) == 0:
    pass
else:
    et = [(-1, 0)] + et
    for i in range(len(et) - 1):
        if et[i][0] <= n <= et[i + 1][0] and et[i][1] == et[i + 1][1]:
            res = et[i][1] + 1
            break
    et = et[1:]
    if res == -1 and et[-1][1] != 0:
        y = []

        for i in range(1, et[-1][0] // et[-1][1] + 1):
            fl = True
            for j in range(len(et)):
                if et[j][0] // i != et[j][1]:
                    fl = False
                    break
            if fl:
                y.append(i)
        y1 = set([(n // tmp + 1) for tmp in y])
        if len(y1) == 1:
            res = y1.pop()
print(res)
