n, m = map(int, input().split())
py = [[i + 1] + list(map(int, input().split())) for i in range(m)]
pysort = sorted(py, key=lambda x: (x[1], x[2]))

j = 1
cnt = 0
for i in range(m):
    while True:
        if pysort[i][1] == j:
            cnt += 1
            pysort[i] += [str(pysort[i][1]).zfill(6) + str(cnt).zfill(6)]
            break
        else:
            cnt = 0
            j += 1

pysortsort = sorted(pysort, key=lambda x: x[0])
[print(a[3]) for a in pysortsort]
