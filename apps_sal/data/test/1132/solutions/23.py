n, m = map(int, input().split())
a = []
for i in range(0, n+1):
    a.append([])
for i in range(m):
    i, j = map(int, input().split())
    a[i].append(j)
    a[j].append(i)
c = 0
d = 0
f = 0
for el in a:
    if(len(el)==1):
        c+=1 
    elif(len(el)==2):
        d+=1 
    elif(len(el)==n-1):
        f+=1 
if(c==2 and d==n-2):
    print("bus topology")
elif(d==n):
    print("ring topology")
elif(f==1 and c==n-1):
    print("star topology")
else:
    print("unknown topology")
