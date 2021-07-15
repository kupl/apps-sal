n,x=map(int, input().split())
l=[]
for i in range(n):
    m=int(input())
    l.append(m)
print(n+((x-sum(l))//min(l)))
