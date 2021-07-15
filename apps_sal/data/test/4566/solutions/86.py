n,m=map(int,input().split())
c=[0]*n
for _ in range(m):
    a,b=[int(j) for j in input().split()]
    c[a-1]+=1
    c[b-1]+=1
for i in c:
    print(i)
