n, m = map(int, input().split())
G = []
L = [[0 for x in range(m + 2)] for x in range(n + 2)]
R = [[0 for x in range(m + 2)] for x in range(n + 2)]
U = [[0 for x in range(m + 2)] for x in range(n + 2)]
D = [[0 for x in range(m + 2)] for x in range(n + 2)]

for i in range(n):
    s = input()
    G.append(s)
    
for i in range(n):
    
    nm = 0
    for j in range(m):
        if(G[i][j] == '*'):
            nm += 1
        else:
            nm = 0
        L[i][j] = nm
        
    nm = 0
    for j in range(m - 1, -1, -1):
        if(G[i][j] == '*'):
            nm += 1
        else:
            nm = 0
        R[i][j] = nm
        
for j in range(m):
    
    nm = 0
    for i in range(n):
        if(G[i][j] == '*'):
            nm += 1
        else:
            nm = 0
        U[i][j] = nm
    
    nm = 0
    for i in range(n - 1, -1, -1):
        if(G[i][j] == '*'):
            nm += 1
        else:
            nm = 0
        D[i][j] = nm

col = [[0 for x in range(m + 2)] for x in range(n + 2)]
row = [[0 for x in range(m + 2)] for x in range(n + 2)]
ANS = []

for i in range(n):
    for j in range(m):
        if(G[i][j] == '.'):
            continue
        ans = min(U[i][j], L[i][j], R[i][j], D[i][j]) - 1
        if(ans <= 0):
            continue
        ANS.append([i + 1, j + 1, ans])
        row[i][j - ans] += 1
        row[i][j + ans + 1] -=1
        col[i - ans][j] += 1
        col[i + ans + 1][j] -= 1
        
        
for i in range(n):
    for j in range(1, m):
        row[i][j] += row[i][j - 1]

for j in range(m):
    for i in range(1, n):
        col[i][j] += col[i - 1][j]
        
okay = True
for i in range(n):
    for j in range(m):
        if(G[i][j] == '*' and row[i][j] == 0 and col[i][j] == 0):
            okay = False
            
if(okay):
    print(len(ANS))
    for x in ANS:
        print(x[0], x[1], x[2])
else:
    print(-1)
