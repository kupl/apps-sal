n = int(input())
max1 = -1
max2 = -1
min1 = 10 ** 9 + 1
min2 = 10 ** 9 + 1
for i in range(n):
    (l, r) = list(map(int, input().split()))
    if l > max1:
        max2 = max1
        max1 = l
        i_max1 = i
    elif l > max2:
        max2 = l
        i_max2 = i
    if r < min1:
        min2 = min1
        min1 = r
        i_min1 = i
    elif r < min2:
        min2 = r
        i_min2 = i
if i_max1 == i_min1:
    print(min2 - max2)
else:
    print(max(min2 - max1, min1 - max2, 0))
