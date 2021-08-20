import math
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
min_x = math.inf
for i in range(len(b)):
    x = (b[i] - a[0]) % m
    if x < min_x:
        new_a = [(y + x) % m for y in a]
        new_a.sort()
        if new_a == b:
            min_x = x
print(min_x)
