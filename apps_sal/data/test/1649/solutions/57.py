a=list(map(int,input().split()))
for i in range(4):
    if a[i]==sum(a)-a[i]:
        print("Yes")
        return
for i in range(4):
    for j in range(i+1,4):
        if a[i]+a[j]==sum(a)-a[i]-a[j]:
            print("Yes")
            return
print("No")
