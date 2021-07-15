n=int(input())
s=input()
MOD=10**9+7
numa=0
numab=0
ans=0
numa1=0
numab1=0
ans1=0
numab2=0
ans2=0
ans3=0
count=0
for i in range(n):
    if s[i]=='a':
        numa=(numa+1)%MOD
    elif s[i]=='b':
        numab=(numab+numa)%MOD
        numab1=(numab1+numa1)%MOD
    elif s[i]=='c':
        ans=(ans+numab)%MOD
        ans1=(ans1+numab1)%MOD
        ans2=(ans2+numab2)%MOD
    else:
        ans1=(ans1+numab)%MOD
        ans2=(ans2+numab1)%MOD
        ans3=(ans3+numab2)%MOD
        numab1=(numab1+numa)%MOD
        numab2=(numab2+numa1)%MOD
        numa1=(numa1+1)%MOD
        count+=1
ans=(ans*pow(3,count,MOD))%MOD
if count>=3:
    ans=(ans+ans3*pow(3,count-3,MOD))%MOD
if count>=2:
    ans=(ans+ans2*pow(3,count-2,MOD))%MOD
if count>=1:
    ans=(ans+ans1*pow(3,count-1,MOD))%MOD
print(ans)
