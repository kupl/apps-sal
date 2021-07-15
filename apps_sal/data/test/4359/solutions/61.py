import sys
import math

a = [int(input()) for i in range(5)]
ans = 0

min = 11
check = True
for i in range(5):
    if (a[i] % 10) < min and (a[i] % 10 != 0):
        min = (a[i] % 10)
        check=False

if check:
    min = 0

b = 100

for j in range(5):

    if a[j] % 10 == min:
        b = j

value = a.pop(b)

for x in a:
    ans += int(math.ceil(x / 10.0)) * 10

ans += value
print(ans)
