x = int(input())
res = []
ok = -1
for i in range(1, 3000001):
    m = i
    tmp = (m - 1) * (m + 1) * m // 6 + x
    if tmp * 2 % (m * (m + 1)) == 0:
        n = int(tmp * 2 // (m * (m + 1)))
        if n > m:
            res.append([i, n])
        if n == m and ok == -1:
            ok = len(res)
            res.append([i, i])
d = 0 if ok == -1 else 1
print(len(res) * 2 - d)
for i in range(len(res)):
    print(str(res[i][0]) + ' ' + str(res[i][1]))
for i in range(len(res)):
    if len(res) - i - 1 != ok:
        print(str(res[len(res) - i - 1][1]) + ' ' + str(res[len(res) - i - 1][0]))
