n = int(input())
min1, max1 = map(int, input().split())
min2, max2 = map(int, input().split())
min3, max3 = map(int, input().split())

a1 = min1
a2 = min2
a3 = min3
n = n - a1 - a2 - a3

max1 -= min1
max2 -= min2
max3 -= min3

if n > max1:
    a1 += max1
    n -= max1
else:
    a1 += n
    n = 0
if n > max2:
    a2 += max2
    n -= max2
else:
    a2 += n
    n = 0
if n > max3:
    a3 += max3
    n -= max3
else:
    a3 += n
    n = 0
print(a1, a2, a3)
