a,b=list(map(str,input().split()))
c=int(a+b)
for i in range(1,1001):
    if i**2==c:
        print("Yes")
        return
print("No")
return

