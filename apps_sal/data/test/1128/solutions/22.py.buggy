import math
ip = list(int(n) for n in input().split())
a = ip[0]
m = ip[1]
while (a % 2 == 0 and m % 2 == 0):
    a /= 2
    m /= 2
a %= m
af = [a]
x = 1
k = 1
count = 0
countlimit = 0
m2 = m
while (m2 % 2 == 0):
    countlimit += 1
    m2 /= 2
while (k == 1):
    a = ((a * 2) % m)
    if a == 0:
        print("Yes")
        k = 0
    else:
        for check in af:
            if a == check:
                print("No")
                k = 0
    if count <= countlimit:
        af.append(a)
        count += 1
return
