N, M = list(map(int, input().split()))
PY = [list(map(int, input().split())) + [i] + [0] for i in range(M)]

PY_sorted = sorted(PY, key=lambda a: (a[0], a[1]))
PY_sorted[0][3] = str(PY_sorted[0][0]).zfill(6) + str(1).zfill(6)
# print(PY_sorted)
cnt = 1
for i in range(1, M):
    cnt += 1
    if PY_sorted[i][0] != PY_sorted[i - 1][0]:
        cnt = 1
        PY_sorted[i][3] = str(PY_sorted[i][0]).zfill(6) + str(cnt).zfill(6)
    else:
        PY_sorted[i][3] = str(PY_sorted[i][0]).zfill(6) + str(cnt).zfill(6)
# print(PY_sorted)
ans = sorted(PY_sorted, key=lambda a: a[2])
for a in ans:
    print((a[3]))
