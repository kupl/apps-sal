n = int(input())
(min1, max1) = (int(x) for x in input().split())
(min2, max2) = (int(x) for x in input().split())
(min3, max3) = (int(x) for x in input().split())
a1 = max1
a2 = max2
a3 = n - a1 - a2
if a3 < min3:
    a2 -= min3 - a3
    a3 = min3
if a2 < min2:
    a1 -= min2 - a2
    a2 = min2
print(a1, a2, a3)
