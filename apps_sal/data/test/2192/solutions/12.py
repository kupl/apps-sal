n = int(input())
w = [None] * n
for i in range(n):
    w[i] = [int(j) for j in input().strip().split(' ')]

for i in range(n):
    for j in range(n):
        val = w[i][j]
        if (i != j):
            val = (val + w[j][i]) / 2
        print('{:.8f}'.format(val), end=' ')
    print('')

for i in range(n):
    for j in range(n):
        val = 0
        if (i != j):
            val = w[i][j] - (w[i][j] + w[j][i]) / 2
        print('{:.8f}'.format(val), end=' ')
    print('')
