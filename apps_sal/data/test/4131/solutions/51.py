(N, M) = map(int, input().split())
PY = [list(map(int, input().split())) for _ in range(M)]
iPY = [[i] + PY[i] for i in range(M)]
iPY.sort(key=lambda x: (x[1], x[2]))
ans = []
cnt = 1
last = -1
for (i, p, y) in iPY:
    if p == last:
        cnt += 1
    else:
        last = p
        cnt = 1
    ans.append([i, str(p).zfill(6) + str(cnt).zfill(6)])
ans.sort()
for a in ans:
    print(a[1])
