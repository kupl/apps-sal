b=[]
r=[]
c=[]
n=int(input())
cnt=0
for i in range(n):
    s=input()
    b.append(s)
m=int(input())
for j in range(m):
    t=input()
    r.append(t)
for i in b:
    cnt += b.count(i)-r.count(i)
    c.append(cnt)
    cnt=0
print(max(max(c),0))
