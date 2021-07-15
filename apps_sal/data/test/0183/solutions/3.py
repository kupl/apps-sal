def get_input():
    hahaha=input()
    (n,k,m)=hahaha.split(sep=None, maxsplit=1000)
    return (int(n),int(k),int(m))
(n,k,m)=get_input()
f=[0 for i in range(k)]   
s=0
for v in range(n):
    tens = 10**v%k
    f=[  (sum(   [f[(j+k-(x+1)*tens)%k] for x in range(9)] )+f[j])%m       for j in range(k)]
    for x in range(9):
        f[(x+1)*tens%k]+=1
    if n-v-1==0:
        s+=(f[0]%m)
    else:
        s+=f[0]*((10**(n-v-2)*9))%m
    f[0]=0
print(s%m)

