import math
str = input()
n = int(str)
a = list(map(int, input().split()))
a.sort()
j = -1
for i in range(0, n - 1):
    a[i] = abs(a[i] - a[i + 1])
    if j == -1:
        j = a[i]
    else:
        j = math.gcd(j, a[i])
sum = 0
for i in range(0, n - 1):
    sum = sum + (a[i] // j - 1)
print(sum)
