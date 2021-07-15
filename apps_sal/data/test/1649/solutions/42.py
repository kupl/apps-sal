l=list(map(int,input().split()))
s=sum(l)/2
for i in range(16):
    tmp=0
    for j in range(4):
        if (i>>j)&1:
            tmp+=l[j]
    if s==tmp:
        print("Yes")
        return
print("No")
