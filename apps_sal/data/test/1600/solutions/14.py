x = int(input())
y = list(map(int, input().split(' ')))
z = y[:]
z.sort()
sumx = 0
b = 0
for i in range(x):
    sumx += y[i] - z[i]
    if sumx == 0:
        b += 1
print(b)
