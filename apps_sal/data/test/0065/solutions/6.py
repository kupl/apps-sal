n=int(input())
a=[int(i) for i in input().split()]
p=[]
z=min(a)
for i in range(n):
    if a[i]==z:
        p.append(i)
x=[]
for i in range(len(p)-1):
    x.append(p[i+1]-p[i])
print(min(x))

