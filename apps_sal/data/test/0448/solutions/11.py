from math import ceil
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list()
for i in a:
    b.append(ceil(i / m))
x = max(b)
last = -1
i = 0
while i < n:
    if b[i] == x:
        last = i
    i += 1
print(last + 1)
