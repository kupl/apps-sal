n = int(input())
a = list(map(int, input().split()))
b = []
f = 1
for i in range(len(a) - 1):
    b.append(abs(a[i] - a[i + 1]) * f)
    f *= -1
max1, max2 = 0, 0
a1, a2 = 0, 0
for i in range(n - 1):
    if a1 + b[i] > 0:
        a1 += b[i]
    else:
        a1 = 0
    max1 = max(a1, max1)
    if a2 - b[i] > 0:
        a2 -= b[i]
    else:
        a2 = 0
    max2 = max(a2, max2)
print(max(max1, max2))

