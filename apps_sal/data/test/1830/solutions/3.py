n, m = map(int, input().split())
xyi = [list(map(int, input().split())) for i in range(m)]
x = [0] * (n + 1)
y = [0] * (n + 1)
numx = 0
numy = 0
num = n * n
for i in range(m):
    if x[xyi[i][0]] == 0:
        num += numy - n
        numx += 1
        x[xyi[i][0]] = 1
    if y[xyi[i][1]] == 0:
        num += numx - n
        numy += 1
        y[xyi[i][1]] = 1
    print(num, end=" ")
