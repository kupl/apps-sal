import math
n = int(input())
d = 0
for i in range(2,int(math.sqrt(n))+1):
    if n%i == 0:
        d = i
        break
if d == 0:
    d = n
if d == 2:
    print(n//d)
else:
    print(1+(n-d)//2)

