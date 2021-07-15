from math import*
n, s = list(map(int, input().split()))
k = [0] * 1001
x = [0] * 1001
y = [0] * 1001
r0 = 0
r = 0
count = 0
Minr = 1000000
otv = -1
for i in range(n):
    x[i], y[i], k[i] = list(map(int, input().split()))
for i in range(n):
    count = s
    r0 = sqrt((x[i]) ** 2 + y[i] ** 2)
    for j in range(n):
        r = sqrt((x[j]) ** 2 + y[j] ** 2)
        if r <= r0:
            count += k[j]
        if count >= 1000000 and r0 < Minr:
            Minr = r0
            otv = r0
            break
print(otv)

            
        

