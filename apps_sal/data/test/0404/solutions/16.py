import math
b = int(input())
k = math.ceil(b ** 0.5) + 100
a = set()
for i in range(1, k):
    if b % i == 0:
        a.add(i)
        a.add(b // i)
print(len(a))
