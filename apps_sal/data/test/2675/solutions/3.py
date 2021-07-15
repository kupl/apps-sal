# cook your dish here
n,m = map(int,input().split())
l = []
c = dict()
for i in range(n):
    x,u = map(int,input().split())
    l.append(x*u) 
for i in range(m):
    y,v = map(int,input().split())
    z = y*v
    if z in c:
        c[z]+=1
    else:
        c[z]=1
co = 0
for i in range(n):
    if l[i] in c and c[l[i]]>0:
        co+=1
        c[l[i]]-=1
print(co)
