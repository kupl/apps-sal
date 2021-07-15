u=set()
v=set()
w=set()
s=set()
def work():
    nonlocal u,v
    if len(u)<3 or len(v)<3:
        return(0)
    u = sorted(list(u))
    v = sorted(list(v))
    for i in range(3):
        for j in range(3):
            if i!=1 or j!=1:
                w.add((u[i],v[j]))
    return(w == s)

for i in range(8):
    x,y = list(map(int,input().split()))
    s.add((x,y))
    u.add(x)
    v.add(y)
    
if work():
    print("respectable")
else:
    print("ugly")

