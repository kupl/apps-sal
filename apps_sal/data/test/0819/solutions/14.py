a, b = map(int, input().split())
c = input().split()
max1 = -1000000000
for i in range (a):
    if int(max1) < int(c[i]):
        ma = i
        max1 = c[i]
min1 = 10000000000
for i in range (a):
    if int(min1) > int(c[i]):
        min1 = c[i]
        mi1 = i
if b >= 3:
    print(max1)
elif b == 1:
    print(min1)
elif b == 2:
    if int(c[0]) < int(c[a - 1]):
        print(int(c[a - 1]))
    else:
        print(int(c[0]))
