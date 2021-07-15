mod = 10**9+7
x = int(input())
y = list(map(int, input().split(' ')))
z = y[:]
z.sort()

prod = 1
sumx = 0

prod2 = 1
sumx2 = 0

b = 0

for i in range(x):
    prod *= y[i]
    sumx += y[i]
    prod2 *= z[i]
    sumx2 += z[i]
    prod %= mod
    prod2 %= mod
    if (prod == prod2 and sumx == sumx2):
        b+=1
        prod=1
        prod2=1
        sumx=0
        sumx2=0

print(b)

