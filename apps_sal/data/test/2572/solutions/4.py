t=int(input())
for _ in range(t):
    n, m=map(int, input().split())
    a=[]
    ans=0
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n//2):
        for j in range(m//2):
            u=[a[i][j], a[i][m-1-j], a[n-1-i][j], a[n-1-i][m-1-j]]
            u.sort()
            ans+=u[2]-u[0]+u[3]-u[1]
    if n%2!=0:
        for j in range(m//2):
            u=[a[n//2][j], a[n//2][m-1-j]]
            u.sort()
            ans+=u[1]-u[0]
    if m%2!=0:
        for i in range(n//2):
            u=[a[i][m//2], a[n-1-i][m//2]]
            u.sort()
            ans+=u[1]-u[0]
    print(ans)
