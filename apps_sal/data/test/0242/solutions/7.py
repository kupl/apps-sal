n=int(input())
l,r=0,n*5
def kil(a):
    s=0
    while a>4: a//=5; s+=a
    return s
a=0
while l<=r:
    s=(l+r)//2
    t=kil(s)
    if t<n: l=s+1
    else: a=s; r=s-1
l=[]
while kil(a)==n:
    l+=[str(a)]; a+=1
print(len(l))
print(' '.join(l))
