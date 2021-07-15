n,x=map(int,input().split())
m=[]
for i in range(n):
    m.append(int(input()))
print((x-sum(m))//min(m)+n)
