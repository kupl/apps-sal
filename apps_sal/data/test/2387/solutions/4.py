n=int(input())
po,ne=[],[]
now=0
for i in range(n):
    p=0
    mp=0
    for j in input():
        p+=(1,-1)[j==")"]
        mp=min(p,mp)
    if mp:
        if p>=0:
            po.append((mp,p))
        else:ne.append((mp-p,-p))
    else:now+=p
po.sort(reverse=1)
ne.sort(reverse=1)
for m,p in po:
    if m+now<0:print("No");return
    else:now+=p
nnow=0
for m,p in ne:
    if m+nnow<0:print("No");return
    else:nnow+=p
print("Yes" if now==nnow else "No") 
