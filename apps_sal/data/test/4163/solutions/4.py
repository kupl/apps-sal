n = int(input())
c=0
yea=False
for i in range(n):
    a,b=list(map(int,input().split()))
    if a==b:
        c+=1
        if c==3:
            yea=True
    else:
        c=0
print(("Yes" if yea else "No"))

