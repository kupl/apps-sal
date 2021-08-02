import math

n = int(input())

a = int(math.sqrt(n))

if a * a == n:
    print(4 * a)
elif a * (a + 1) >= n:
    print(4 * a + 2)
else:
    print(4 * (a + 1))
