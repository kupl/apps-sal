import math
n = int(input())
top = int(math.sqrt(n))
a = 1
for x in range(1, top + 1):
    if n % x == 0:
        a = x
a_pair = n // a
print(a + a_pair - 2)
