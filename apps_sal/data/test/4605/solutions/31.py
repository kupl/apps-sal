n,a,b = map(int,input().split())
c = 0
for i in range(1,n+1):
    s = 0
    d = i
    while d!=0:
        s+= d%10
        d//=10
    if a<=s<=b:
        c+=i
print(c)
