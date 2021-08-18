n, m = map(int, input().split())

M1 = []
M2 = []

for i in range(n):
    M1.append(list(map(int, input().split())))

for i in range(n):
    M2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        M1[i][j], M2[i][j] = min(M1[i][j], M2[i][j]), max(M1[i][j], M2[i][j])

f = 1
for i in range(n):
    for j in range(m):
        if i > 0 and (M1[i][j] <= M1[i - 1][j] or M2[i][j] <= M2[i - 1][j]):
            f = 0
            break
        if j > 0 and (M1[i][j] <= M1[i][j - 1] or M2[i][j] <= M2[i][j - 1]):
            f = 0
            break
if f == 1:
    print("Possible")
else:
    print("Impossible")
