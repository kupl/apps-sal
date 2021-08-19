(N, M) = list(map(int, input().split()))
PY = [list(map(int, input().split())) + [i] for i in range(M)]
PY.sort(key=lambda x: x[1])
ans = []
cnt = [0] * N
for (p, y, i) in PY:
    ans.append(('{0:06d}'.format(p) + '{0:06d}'.format(cnt[p - 1] + 1), i))
    cnt[p - 1] += 1
ans.sort(key=lambda x: x[1])
for a in ans:
    print(a[0])
