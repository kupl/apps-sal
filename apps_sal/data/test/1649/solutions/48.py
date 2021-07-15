a=list(map(int,input().split()))
a=sorted(a)
b=a[0]+a[3]
c=a[1]+a[2]
if b==c:
  print("Yes")
else:
  if a[0]+a[1]+a[2]==a[3]:
    print("Yes")
  else:
    print("No")
