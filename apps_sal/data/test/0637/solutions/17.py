# python3



n = input()
a = list(map(int, input().split()))
len=0

n=int(n)

len=0

for i in range (1,n):
    sc = a[i]-a[i-1]
    if(sc>0):
        len=i
        break
    if(sc<0):
        len=i
        break
fl=1;
if(len==0): 
    len=n
r=n%len
if(r==0):
    lol=1
else:
    print("NO")
    return
for i in range (1,n):
    sc = a[i]-a[i-1]
    if(sc>0):
        tmp = (i)%len
        if(tmp>0):
            fl=0
        if(tmp<0):
            fl=0
    if(sc<0):
        tmp = (i)%len
        if(tmp>0):
           fl=0
        if(tmp<0):
            fl=0
    if(sc==0):
        tmp = (i)%len
        if(tmp==0):
            fl=0
if(fl==0):
    print ("NO")
else:
    print("YES")
