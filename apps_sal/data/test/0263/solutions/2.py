from math import ceil

n = int(input())
m = int(input())

bs = []
for _ in range(n):
    bs.append(int(input()))

b = max(bs)
total = sum(bs) + m

maximum = b + m
if total <= b * n:
    minimum = b
else:
    minimum = int(ceil(total / n))

print(minimum, maximum)

