n,m = [int(i) for i in input().split()]
b=[]
a=[]
for i in range(n):
    b.append([i for i in input()])
    a.append([0 for i in range(m)])
    
def check(e,r,q):
    if e>=0 and r>=0 and e+2<n and r+2<m:
        if b[e][r]=='#' and b[e+1][r]=='#' and b[e+2][r]=='#' and b[e+2][r+1]=='#' and b[e+2][r+2]=='#' and b[e+1][r+2]=='#' and b[e][r+2]=='#' and b[e][r+1]=='#':
            a[e][r]==1 
            a[e+1][r]==1 
            a[e+2][r]==1
            a[e+2][r+1]==1
            a[e+2][r+2]==1  
            a[e+1][r+2]==1
            a[e][r+2]==1 
            a[e][r+1]==1
            return True
    if q ==1:
        return False
    return check(e,r-1,1) or check(e,r-2,1) or check(e-1,r-2,1) or check(e-2,r-2,1) or check(e-2,r-1,1) or check(e-2,r,1) or check(e-1,r,1)
for i in range(n):
    for j in range(m):
        if b[i][j]=='#':
            if (not check(i,j,0)) and a[i][j]==0:
                print("NO")
                return
print("YES")
