n,m=list(map(int,input().split()))
flag = 0
for i in range(m):
    s=0
    q = set()
    a = list(map(int,input().split()))
    for item in a[1:]:
        if(-item in q):
            s=1
        q.add(item)
    if(s==0):
        flag=1
if(flag):
    print("YES")
else:
    print("NO")
        

