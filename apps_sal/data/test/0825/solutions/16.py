import math

n = int(input())
d = n
m = {}

for i in range(2, int(math.sqrt(n)) + 1):
    m[i] = 0
    while (d % i == 0):
        d //= i
        m[i] += 1
res = 0
for i in list(m.values()):
    res += int(math.sqrt(i * 2 + 0.25) - 0.5)

if d > 1:
    res += 1
print(res)
