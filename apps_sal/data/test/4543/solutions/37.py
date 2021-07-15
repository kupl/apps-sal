a,b=list(map(str,input().split()))
c=a+b
c=int(c)
for i in range(1001):
  if i**2==c:
    print("Yes")
    return
print("No")

