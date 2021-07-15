
def sum_matr(matr):
    for i in (0, n-1):
        for j in range(m-1):
            if matr[i][j] >= matr[i][j+1]:
                return -1
    for j in (0, m-1):
        for i in range(n-1):
            if matr[i][j] >= matr[i+1][j]:
                return -1
    for i in range(n-2,0,-1):
        for j in range(m-2,0,-1):
            if matr[i][j] == 0:
                c = min(matr[i][j+1] - 1, matr[i+1][j] - 1)
                if c <= matr[i][j-1] or c <= matr[i-1][j]:
                    return -1
                else:
                    matr[i][j] = c
            elif matr[i][j] >= matr[i+1][j] or matr[i][j] >= matr[i+1][j]:
                return -1
    s = 0
    for i in range(n):
        for j in range(m):
            s += matr[i][j]
    return s

n, m = [int(elem) for elem in input().split()]
matr = []
for i in range(n):
    matr.append([int(elem) for elem in input().split()])
    
print(sum_matr(matr))

