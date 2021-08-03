N, M = list(map(int, input().split()))
PY = []
for i in range(M):
    PY.append([i] + list(map(int, input().split())))

PY.sort(key=lambda x: x[2])
ans = []
C = [0] * (N + 1)
for i, P, Y in PY:
    C[P] += 1
    ans.append([i, '{:0=6}{:0=6}'.format(P, C[P])])
ans.sort()
for i, a in ans:
    print(a)
