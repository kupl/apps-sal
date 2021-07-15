inp=input().split(" ")
n=inp[0]
ss=0
a=[]
g=[]
inp1=input().split(" ")
p=[]
z=0

for i in range(int(n)):
    a.append(int(inp1[i]))
ans=0
s=0
for i in range(len(a)):
    s+=a[i]
if s%3!=0:
    print('0')
else:
    s//=3
    ss=0
    k=0
    l=0
    for n in a:
        k+=n
        if s==0:
            if k==0:
                l+=1
                continue
        if k==s:
            l+=1
        if k==s*2:
            ans+=l
    if s==0:
        print(((l-1)*(l-2))//2)
    else:
        print(ans)
