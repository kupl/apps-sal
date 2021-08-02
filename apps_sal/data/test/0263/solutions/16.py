import math
n = int(input())
m = int(input())
x = m

arr = []
for i in range(n):
    arr.append(int(input()))

maxx = max(arr)

summ = 0

for i in range(n):
    if arr[i] <= maxx:
        if m >= maxx - arr[i]:
            m -= maxx - arr[i]
            arr[i] = maxx
        else:
            arr[i] += m
            m = 0

print(maxx + math.ceil(m / n), maxx + x)
