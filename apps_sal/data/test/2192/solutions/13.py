size = int(input())
w = []

for enu in range(size):
    temp = input().split()
    w.append(list(map(int, temp)))
A = [[0 for i in range(size)] for j in range(size)]
B = [[0 for i in range(size)] for j in range(size)]
for i in range(size):
    for j in range(i, size):
        A[i][j] = (w[i][j] + w[j][i]) / 2
        B[i][j] = (w[i][j] - w[j][i]) / 2
        A[j][i] = A[i][j]
        B[j][i] = -B[i][j]
def pr(A):
    nonlocal size
    for i in range(size):
        for j in range(size - 1):
            print("%.8f" % A[i][j], end = ' ')
        print('%.8f' % A[i][-1])
pr(A)
pr(B)
