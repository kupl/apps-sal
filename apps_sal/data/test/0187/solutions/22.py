n = int(input())
A = []
D = {}
k = []
for i in range(n):
    x = int(input())
    A.append(x)
    if x not in D:
        D[x] = 0
        k.append(x)
    D[x] += 1
if len(D) != 2:
    print('NO')
elif D[k[0]] == D[k[1]]:
    print('YES')
    print(k[0], k[1])
else:
    print('NO')
