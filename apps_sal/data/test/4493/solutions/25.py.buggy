C = [list(map(int, input().split())) for _ in range(3)]
x = [0, 0, 0]
y = [0, 0, 0]

for i in range(3):
    y[i] = C[0][i]
for i in range(3):
    x[i] = C[i][0] - y[0]
for i in range(3):
    for j in range(3):
        if C[i][j] != x[i] + y[j]:
            print('No')
            return
print('Yes')
