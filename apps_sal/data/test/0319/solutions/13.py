(m, n) = map(int, input().split())
D1 = {}
D2 = {}
for i in range(m):
    D1[i] = []
for i in range(n):
    D2[i] = []
for i in range(m):
    L = input()
    for j in range(n):
        if L[j] == '1':
            D1[i].append(j)
            D2[j].append(i)
X = 0
for i in range(m):
    E = 0
    for j in D1[i]:
        if len(D2[j]) == 1:
            E = 1
            break
    if E == 0:
        X = 1
        break
if X == 1:
    print('YES')
else:
    print('NO')
