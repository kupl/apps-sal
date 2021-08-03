import sys
input = sys.stdin.readline
n, m = map(int, input().split())
matrix = [0] * n
for i in range(n):
    line = input()
    matrix[i] = [0] * m
    for j in range(m):
        matrix[i][j] = int(line[j])
if n > m:
    matrix2 = [0] * m
    for i in range(m):
        matrix2[i] = [0] * n
        for j in range(n):
            matrix2[i][j] = matrix[i][j]
    n, m = m, n
    matrix = [0] * n
    for i in range(n):
        matrix[i] = [0] * m
        for j in range(m):
            matrix[i][j] = matrix2[i][j]
if n > 3:
    print(-1)
else:
    if n == 1:
        print(0)
    else:
        if n == 2:
            poss = [[0, 0], [1, 0], [1, 1], [0, 1]]
            costs = [0] * 4
            for i in range(m):
                newcosts = [0] * 4
                for p in range(4):
                    bc = 0
                    for foo in range(2):
                        if poss[p][foo] != matrix[foo][i]:
                            bc += 1
                    newcosts[p] = min(costs[p - 1], costs[(p + 1) % 4])
                    newcosts[p] += bc
                for p in range(4):
                    costs[p] = newcosts[p]
            print(min(costs))
        else:
            poss1 = [[0, 0, 0], [0, 1, 0], [1, 1, 1], [1, 0, 1]]
            poss2 = [[1, 0, 0], [1, 1, 0], [0, 1, 1], [0, 0, 1]]
            costs1 = [0] * 4
            costs2 = [0] * 4
            for i in range(m):
                newcosts1 = [0] * 4
                newcosts2 = [0] * 4
                for p in range(4):
                    bc1 = 0
                    bc2 = 0
                    for foo in range(3):
                        if poss1[p][foo] != matrix[foo][i]:
                            bc1 += 1
                        if poss2[p][foo] != matrix[foo][i]:
                            bc2 += 1
                    newcosts1[p] = min(costs1[p - 1], costs1[(p + 1) % 4])
                    newcosts1[p] += bc1
                    newcosts2[p] = min(costs2[p - 1], costs2[(p + 1) % 4])
                    newcosts2[p] += bc2
                for p in range(4):
                    costs1[p] = newcosts1[p]
                    costs2[p] = newcosts2[p]
            print(min(min(costs1), min(costs2)))
