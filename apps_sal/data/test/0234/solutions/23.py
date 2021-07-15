a=[]
n,N=list(map(int,input().split()))
for i in range(n):
    a.append(input())
for i in range(n):
    for j in range(N):
        m=(i and a[i-1][j]=='*')+(j and a[i][j-1]=='*')+(i<n-1 and a[i+1][j]=='*')+(j<N-1 and a[i][j+1]=='*')+(i and j and a[i-1][j-1]=='*')+(i<n-1 and j<N-1 and a[i+1][j+1]=='*')+(i and j<N-1 and a[i-1][j+1]=='*')+(i<n-1 and j and a[i+1][j-1]=='*')
        if a[i][j]=='.' and m!=0 or '1'<=a[i][j]<='8' and int(a[i][j])!=m:
            print('NO')
            return
print('YES')
        
            
    

