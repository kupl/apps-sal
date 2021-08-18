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
    for row in A:
        for i, entry in enumerate(row):
            print("{0:.8f}".format(entry), end=sep(i))


def sep(i):
    nonlocal size
    if i >= size - 1:
        return '\n'
    else:
        return ' '


pr(A)
pr(B)
