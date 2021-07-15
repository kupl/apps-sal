a,b=input().split()

d=int(a+b)

for i in range(1000):
    if d==i**2:
        print("Yes")
        break

lis=[j**2!=d for j in range(1000)]
if all(lis)==True:
    print("No")

