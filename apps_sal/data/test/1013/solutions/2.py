(n, m) = list(map(int, input().split()))
L = []
C = []
for i in range(n):
    L.append(list(map(int, input().split())))
case = False
for i in range(n):
    if L[i][0] == 1 or L[i][m - 1] == 1:
        case = True
for i in range(m):
    if L[0][i] == 1 or L[n - 1][i] == 1:
        case = True
if case:
    print(2)
else:
    print(4)
