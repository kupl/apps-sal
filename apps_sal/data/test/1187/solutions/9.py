n,m=[int(x) for x in input().split()]
dic={}
paint={}
cycle=False
edges=[]
for i in range(m):
    a,b=[int(x) for x in input().split()]
    edges.append((a,b))
    if a not in dic:
        dic[a]=set([b])
    else:
        dic[a].add(b)
inv=[False]*(n+1)
invite=[False]*(n+1)
def gcd(n):
    paint[n]=0
    invite[n]=True
    if n in dic:
        for item in dic[n]:
            if not invite[item]:
                if gcd(item):
                    return True
            else:
                if paint[item]==0:
                    return True
    paint[n]=1
    return False
for item in range(1,n+1):
    if not invite[item]:
        cycle=gcd(item) or cycle
arr=[]
if cycle:
    print(2)
    for item in edges:
        if item[0]<item[1]:
            arr.append(1)
        else:
            arr.append(2)
else:
    print(1)
    for item in edges:
        arr.append(1)
print(*arr)
    

