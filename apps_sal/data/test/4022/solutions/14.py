n = int(input())
(min1, min2) = ([10 ** 10, 0], [10 ** 10, 0])
(max1, max2) = ([-1, 0], [-1, 0])
a = [0] * n
for i in range(n):
    x = list(map(int, input().split()))
    a[i] = x
    if min1[0] >= x[1]:
        min2 = min1
        min1 = [x[1], i]
    elif min2[0] >= x[1]:
        min2 = [x[1], i]
    if max1[0] <= x[0]:
        max2 = max1
        max1 = [x[0], i]
    elif max2[0] <= x[0]:
        max2 = [x[0], i]
ans = 0
if min1[1] == max1[1]:
    ans = max(ans, min2[0] - max2[0])
else:
    ans = max(ans, min2[0] - max1[0], min1[0] - max2[0])
print(ans)
