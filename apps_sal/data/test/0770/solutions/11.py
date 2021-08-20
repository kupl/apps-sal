import math
n = int(input())
array = list(map(int, input().split(' ')))
ar = []
total = 0
for i in range(n):
    if array[i] == 0:
        total += 1
    else:
        if total > 0:
            ar.append(total)
        total = 0
if array[0] == 1:
    pass
elif len(ar) > 0:
    ar.remove(ar[0])
totalread = 0
totalmove = len(ar)
for i in range(n):
    if array[i] == 1:
        totalread += 1
print(totalread + totalmove)
