from string import *
a = [0] * 64
for i in range(64):
    for j in range(64):
        a[i & j] += 1
x = 1
s = digits + ascii_uppercase + ascii_lowercase + '-_'
for y in input():
    x = x * a[s.index(y)] % 1000000007
print(x)
