import math
n = int(input())
a = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)
x = n * [None]
for i in range(n):
    solved = False
    for j in range(n):
        for k in range(n):
            if i != j and j != k and (k != i):
                xi = int(math.sqrt(a[i][j] * a[i][k] / a[k][j]))
                x[i] = xi
                solved = True
                break
        if solved:
            break
print(' '.join(list(map(str, x))))
