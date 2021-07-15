x = int(input())
y = list(map(int, input().split(' ')))
z = y[:]
z.sort()

sumx = 0
sumx2 = 0

b = 0

for i in range(x):
    sumx += y[i]
    sumx2 += z[i]
    if (sumx == sumx2):
        b+=1


print(b)
