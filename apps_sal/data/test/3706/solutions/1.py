n, m = input().strip().split()
n, m = int(n), int(m)
g = [[int(j) for j in input().strip().split()] for i in range(n)]

answer = []


def b():
    for i in range(n):
        minRow = min(g[i])
        if minRow != 0:
            for k in range(minRow):
                answer.append("row " + str(i + 1))
            for j in range(m):
                g[i][j] -= minRow


def a():
    for j in range(m):
        minCol = g[0][j]
        for i in range(n):
            if g[i][j] < minCol:
                minCol = g[i][j]
        if minCol != 0:
            for k in range(minCol):
                answer.append("col " + str(j + 1))
            for i in range(n):
                g[i][j] -= minCol


if(n < m):
    b()
    a()
else:
    a()
    b()
maxNumber = max(max(g))
if maxNumber == 0:
    print(len(answer))
    for el in answer:
        print(el)
else:
    print("-1")
