import sys
def ma():
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        a.append([*map(int,sys.stdin.readline().split())])
    if a[n-1][m-1] <= a[n-2][m-1] or a[n-1][m-1] <= a[n-1][m-2]:
        return print(-1)
    for i in range(n-2,0,-1):
        for j in range(m-2,0,-1):
            if a[i][j] <= a[i+1][j] or a[i][j] <= a[i][j+1]:
                mi = min(a[i+1][j],a[i][j+1])-1
                if a[i][j] == 0:
                    
                    a[i][j] = min(a[i+1][j],a[i][j+1])-1
                if mi <= a[i-1][j] or mi <= a[i][j-1]:
                        return print(-1)
            else:
                return print(-1)
    su = 0
    for i in range(n):
        su += sum(a[i])
    print(su)
    
ma()

