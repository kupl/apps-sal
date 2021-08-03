import math

n, d = input().split()
count = 0
dn = int(d)

for i in range(int(n)):
    x = list(map(int, input().split()))
    if dn >= math.sqrt(x[0] ** 2 + x[1] ** 2):
        count += 1

print(count)
