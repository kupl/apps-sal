N,K,*L=[int(a)for a in open(0).read().split()]
L,c=sorted(zip(L[::2],L[1::2])),1
for a,b in L:
    c+=b
    if c>K:print(a);return
