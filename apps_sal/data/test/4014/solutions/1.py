n, m = list(map(int, input().split()))
L = []
for i in range(m):
    a, b, c = list(map(int, input().split()))
    L.append([b, a, c, i])
L.sort()

M = [-1 for i in range(n + 1)]
for i in range(m):
    M[L[i][0]] = m + 1
for i in range(1, n + 1):
    if M[i] == -1:
        f = False
        for j in range(m):
            if L[j][1] <= i and L[j][2] > 0 and i < L[j][0]:
                M[i] = L[j][3] + 1
                L[j][2] -= 1
                f = True
                break
        if not(f):
            M[i] = 0
f = True
for j in range(m):
    if L[j][2] > 0:
        f = False
if f:
    print(*M[1:])
else:
    print(-1)
