l,r,x,y,k=map(int,input().split())
for i in range(x,y+1):
    q=k*i
    if q<=r and q>=l:
        print('YES')
        return
print('NO')
