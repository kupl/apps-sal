n=int(input())
ans=[['*']*n for i in range(n)]
for i in range(n//2):
    for j in range(n//2-i,n//2+i+1):
        ans[i][j]='D'
for i in range(n):
    ans[n//2][i]='D'
for i in range(n//2+1,n):
    ans[i]=ans[n-i-1]   
for i in range(n):
    for j in range(n):
        print(ans[i][j],end='')
    print('')
