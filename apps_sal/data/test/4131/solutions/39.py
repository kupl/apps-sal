(N, M) = list(map(int, input().split()))
PY = [list(map(int, input().split())) + [i] for i in range(M)]
sortPY = sorted(PY, key=lambda x: x[1])
prefec = [0] * (N + 1)
res = []
for (p, y, i) in sortPY:
    prefec[p] += 1
    strp = str(p)
    ID = '0' * (6 - len(strp)) + strp + '0' * (6 - len(str(prefec[p]))) + str(prefec[p])
    res.append([ID, i])
sortres = sorted(res, key=lambda x: x[1])
for i in range(M):
    print(sortres[i][0])
