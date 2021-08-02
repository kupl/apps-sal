n = int(input())
min1, max1 = [int(c) for c in input().split()]
min2, max2 = [int(c) for c in input().split()]
min3, max3 = [int(c) for c in input().split()]

a, b, c = 0, 0, 0
if n - min3 <= max1 + max2:
    c = min3
else:
    c = n - max1 - max2

if n - c - min2 <= max1:
    b = min2
    a = n - c - b
else:
    a = max1
    b = n - c - a

print(str(a) + ' ' + str(b) + ' ' + str(c))
