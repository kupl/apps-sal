n=int(input())
comp=list(map(int,input().split(' ')))
done=0
checked=[]
c=0
t=-1
d=-1
while done<n:
    t+=1
    d*=-1
    if 0 not in checked:
        if comp[0]==0:
            done+=1
            checked.append(0)
    c+=d
    while c>=0 and c<n:
        if c not in checked:
            if comp[c]<=done:
                done+=1
                checked.append(c)
        c+=d
print(t)
