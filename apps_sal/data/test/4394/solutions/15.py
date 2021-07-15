n,m = list(map(int,input().split()))
     
l = []
for i in range(m):
    a,b,c = list(map(int,input().split()))
    l.append((c,a,b))
l.sort()
f = [i for i in range(n+1)]
def r(a):
    if a!=f[a]:
        f[a]=r(f[a])
    return f[a]
     
cnt = 0
i=0
while i < m:
    j = i
    while j < m and l[j][0] == l[i][0]:
        j=j+1
    num=0
    for k in range(i,j):
        x=r(l[k][1])
        y=r(l[k][2])
        if x!=y:
            num=num+1
    for k in range(i,j):
        x = r(l[k][1])
        y = r(l[k][2])
        if x != y:
            f[y]=x
            num = num -1
    cnt=cnt+num
    i=j
print(cnt)

