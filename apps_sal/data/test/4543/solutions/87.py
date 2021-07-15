a,b=map(str,input().split())
c=a+b
for i in range(1,350):
    if int(c)==i**2:
        print("Yes")
        break
else:
    print("No")
