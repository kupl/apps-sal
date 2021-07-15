Nlist=list(map(str,input()))
a=0
for i in range(len(Nlist)):
    a+=int(Nlist[i])
N=int(''.join(Nlist))
if N%a==0:
    print('Yes')
else:
    print('No')
