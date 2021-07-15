n=int(input())
a=[]
for i in range(n):
    a.append(list(input()))
for i in range(1,n-1):
    for j in range(1,n-1):
        if a[i][j]=='#' and a[i+1][j]=='#' and a[i-1][j]=='#' and a[i][j-1]=='#' and a[i][j+1]=='#':
            a[i][j]='.'
            a[i][j+1]='.'
            a[i][j-1]='.'
            a[i+1][j]='.'
            a[i-1][j]='.'
for i in a:
    for j in i:
        if j=='#':
            print('NO')
            return
print('YES')


