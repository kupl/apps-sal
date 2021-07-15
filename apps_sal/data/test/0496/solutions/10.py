a=list(map(int,input().split()));n=len(a);o=1;d=a[1]-a[0];ok=1
for i in range(n-1):
    if(a[i+1]-a[i]!=d):ok=0
if(ok):
    print(a[n-1]+d)
    o=0
d=a[1]/a[0];ok=1
for i in range(n-1):
    if(a[i+1]/a[i]!=d):ok=0
if(ok and o):
    o=0
    if(int(a[n-1]*d)==a[n-1]*d):print(int(a[n-1]*d))
    else:o=1
if(o):print(42)
