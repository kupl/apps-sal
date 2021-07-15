import math
n = int(input())
f = list(map(int,input().split()))

f.sort()
diff = f[-1] - f[0]
a = f[0]
b = f[-1]

c1 = 1
c2 = 1
for i in range(1,n-1):
    if f[i] == a :
        c1 += 1
    elif f[i] == b:
        c2 += 1
#print(c1,c2)
if a==b :
    summ = 0
    for i in range(n-1,0,-1):
        summ += i
        
    print(diff,summ )
else:
    print(diff, c1*c2)

