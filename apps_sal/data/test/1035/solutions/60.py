from math import gcd, sqrt, floor
(a, b) = map(int, input().split())
c = gcd(a, b)
x = []
for i in range(1, floor(sqrt(c)) + 1):
    if c % i == 0:
        x.append(i)
        x.append(c // i)
x.sort()
y = []
i = 1
while c > 1 and i < len(x):
    if c % x[i] == 0:
        y.append(x[i])
        c = c // x[i]
    else:
        i += 1
print(len(set(y)) + 1)
