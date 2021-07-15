a1,b1=list(map(int,input().split()))
a=[0]*40
b=[0]*40
A=a1
B=b1
for i in range(1,41):
    a[-i]=a1%2
    b[-i]=b1%2
    a1=a1//2
    b1=b1//2
ans=[0]*40
if a[-1]==1:
    if (a[-2]-b[-2])%2==0:
        if b[-1]==1:
            ans[-1]=1
    else:
        if b[-1]==0:
            ans[-1]=1
else:
    if (a[-2]-b[-2])%2==0:
        if b[-1]==1:
            ans[-1]=1
    else:
        if b[-1]==0:
            ans[-1]=1
for i in range(2,41):
    if a[-i]==1 and a[-1]==1:
        if b[-i]==1 and b[-1]==0:
            ans[-i]=0
        else:
            ans[-i]=1
    else:
        if b[-i]==1 and b[-1]==0:
            ans[-i]=1
        else:
            ans[-i]=0
ans1=0
for i in range(1,41):
    ans1+=(2**(i-1))*ans[-i]
print(ans1)

