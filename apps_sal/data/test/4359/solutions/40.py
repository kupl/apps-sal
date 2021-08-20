import math
n = 5
r = 0
rem = 10
for _ in range(n):
    a = int(input())
    if a % 10 != 0:
        rem = min(rem, a % 10)
    r += math.ceil(a / 10)
print(int(r * 10) - 10 + rem)
