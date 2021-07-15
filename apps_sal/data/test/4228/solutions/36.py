N,L=map(int,input().split())
s=0
l=[]
for i in range(N):
    s+=L+i
    l.append(abs(L+i))
l=sorted(l)
if l[0]<=L:
    s-=l[0]
else:
    s+=l[0]
print(s)
