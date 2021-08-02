a, b = input().split()
a = int(a)
b = int(b)
c = [input().split() for i in range(a)]
d = 1001
for i in range(a):
    if int(c[i][1]) <= b:
        if d > int(c[i][0]):
            d = int(c[i][0])
if d == 1001:
    print("TLE")
else:
    print(d)
