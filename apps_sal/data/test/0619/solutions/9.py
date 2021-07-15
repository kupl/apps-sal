x,y,z=map(int,input().split())
print((x+y)//z,end=" ")
a=x%z
b=y%z
if a+b>=z:
    print(z-max(a,b))
else:
    print("0")

