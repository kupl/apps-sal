n = int(input())
x = list(map(int, input().split()))
a = 0
b = 0
c = 0
d = 0
e = 0
for i in range(n):
    if x[i] == 1:
        a += 1
    if x[i] == 2:
        b += 1
    if x[i] == 3:
        c += 1
    if x[i] == 4:
        d += 1
    if x[i] == 6:
        e += 1
    if x[i] == 5 or x[i] == 7:
        print(-1)
        return
if a != b + c or b + c != d + e or c > e:
    print(-1)
    return
for i in range(d):
    print(1, 2, 4)
b -= d
for i in range(b):
    print(1, 2, 6)
for i in range(c):
    print(1, 3, 6)
