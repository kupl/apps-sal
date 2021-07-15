f = lambda: list(map(int, input().split()))

n, m, q = f()

p = [[0] * m for j in range(n)]

for t in [list(f()) for k in range(q)][::-1]:

    j = t[1] - 1

    if t[0] == 1: p[j].insert(0, p[j].pop())

    elif t[0] == 2: 

        s = p[-1][j]

        for i in range(n - 1, 0, -1): p[i][j] = p[i - 1][j]

        p[0][j] = s

    else: p[j][t[2] - 1] = t[3]

for d in p: print(*d)




# Made By Mostafa_Khaled

