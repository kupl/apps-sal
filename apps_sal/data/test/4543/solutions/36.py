import math
a = input("").split(" ")
a = [int(aa) for aa in a]
n = int(str(a[0])+str(a[1]))
r = math.sqrt(n)
if r**2 == int(r)**2:
    print("Yes")
else:
    print("No")
