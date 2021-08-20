n = int(input())
a = {}
for i in range(1, n + 1):
    a[i] = 0
(max1, max2) = (0, 0)
for i in map(int, input().split()):
    if i < max1:
        if i > max2:
            a[max1] += 1
            max2 = i
    else:
        a[i] -= 1
        max2 = max1
        max1 = i
m = -100
for i in a:
    if a[i] > m:
        m = a[i]
        ans = i
print(ans)
