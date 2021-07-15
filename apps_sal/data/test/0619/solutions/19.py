r=[int(x) for x in input().split()]
m=r[0]
n=r[1]
z=r[2]

maxNum=(m+n)//z
if (m//z+n//z)==(m+n)//z:
    minSwitch=0
else:
    minSwitch=z-max(m % z, n % z)

print(maxNum,end=" ")
print(minSwitch)
