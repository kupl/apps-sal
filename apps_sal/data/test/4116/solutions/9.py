n=int(input())
ans=-1
for i in range(1,10):
    for j in range(1,10):
        if n==i*j:
            ans=1
            break
if ans==1:
    print("Yes")
else:
    print("No")
