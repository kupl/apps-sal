import math
n = int(input())
a = [int(x) for x in input().split()]
b = []
for item in a:
    if item >= 0:
        b.append(-item - 1)
    else:
        b.append(item)
if n % 2 == 1:
    counter = 0
    for item in b:
        if abs(item) >= abs(counter):
            counter = abs(item)
    for i in range(n):
        if abs(b[i]) == abs(counter):
            b[i] = abs(counter) - 1
            break
print(*b)
