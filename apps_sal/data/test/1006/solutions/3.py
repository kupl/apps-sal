n=int(input())
a=[[] for i in range(n)]
for i in range(n):
    s=input().strip()
    for j in s:
        a[i]+=[j]
kr=0
for i in range(n):
    for j in range(n):
        #print(i,j)
        if a[i][j]=='#':
            kr+=1
        if 0<i<n-1 and 0<j<n-1 and a[i][j]=='#':
            if a[i][j-1]==a[i][j+1]==a[i-1][j]==a[i+1][j]=='#':
                kr-=3
                a[i][j-1],a[i][j+1],a[i-1][j],a[i+1][j],a[i][j]='.','.','.','.','.'
if kr:
    print('NO')
else:
    print('YES')
