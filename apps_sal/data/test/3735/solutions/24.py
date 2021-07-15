"""n=int(input())
s=input()
c=0
for i in range(0,len(s)):
    if(s[i]=='8'):
        c=c+1
k=len(s)//11
print(min(c,k))"""


n=int(input())
N=str(n)
if(len(N)==1):
    print(n)
else:
    l=len(N)-1
    k=int('9'*l)
    diff=n-k
    D=str(diff)
    K=str(k)
    sumu=0
    for i in range(0,len(D)):
        sumu=sumu+int(D[i])
    for i in range(0,len(K)):
        sumu=sumu+int(K[i])
    print(sumu)


