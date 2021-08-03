N, M = map(int, input().split())
py = [list(map(int, input().split()))for _ in range(M)]
epy = list(enumerate(py))
P = [[]for _ in range(N + 1)]
for x in epy:
    P[x[1][0]].append(x)

i = 1
ans = []
while i <= N:
    L = P[i]
    L.sort(key=lambda x: x[1])
    j = 0
    while j < len(L):
        L[j][1][1] = j + 1
        ans.append(L[j])
        j += 1
    i += 1
ans.sort()

for e, py in ans:
    p, y = map(str, py)
    p = '0' * (6 - len(p)) + p
    y = '0' * (6 - len(y)) + y
    print(p + y)
