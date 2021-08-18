n = int(input())
a = input().split(" ")
x1 = int(a[0])
x2 = int(a[1])
coor1 = []
coor2 = []
eps = 0.000000001
for i in range(n):
    a = input().split(" ")
    k = int(a[0])
    b = int(a[1])
    coor1.append((k * (x1 + eps) + b, i))
    coor2.append((k * (x2 - eps) + b, i))
coor1.sort()
coor2.sort()
s = "NO"
for i in range(len(coor1)):
    if (coor1[i][1] != coor2[i][1]):
        s = "YES"
print(s)
