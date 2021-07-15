n , m = list(map(int, input().split()))
s = ['#' * (m+2)]
for i in range(n):
    s += ['#'+input()+'#']
s+= ['#' * (m+2)] 
u = [[0 for i in range(m+2)] for j in range(n+2)]
r = [[0 for i in range(m+2)] for j in range(n+2)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if s[i][j] == '.':
            if s[i+1][j] == '.':
                u[i][j] = 1
            if s[i][j+1] == '.':
                r[i][j] = 1
        u[i][j]+= u[i-1][j]+u[i][j-1]-u[i-1][j-1]
        r[i][j]+= r[i-1][j]+r[i][j-1]-r[i-1][j-1]
q = int(input())
for i in range(q):
    A = 0
    x, y, a, b = list(map(int, input().split()))
    if x == a and y == b:
        A = 0
    else:
        A += r[a][b-1]-r[x-1][b-1]-r[a][y-1]+r[x-1][y-1]
        A += u[a-1][b]-u[x-1][b]-u[a-1][y-1]+u[x-1][y-1]
    print(A)


