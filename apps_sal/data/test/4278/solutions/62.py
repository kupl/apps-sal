N=int(input())
d={}
c=0
for i in range(N):
    s=''.join(sorted(input()))
    if s in d:
        c+=d[s]
        d[s]+=1
    else:
        d[s]=1
print(c)
