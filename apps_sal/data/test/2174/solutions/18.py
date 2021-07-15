n=int(input())
p=input().split()
a=[]
for i in range(n):
    a.append(int(p[i]))
    i=i+1
a.sort()
c=0
for i in range(n):
    c=c+abs((i+1)-a[i])
print(c)

