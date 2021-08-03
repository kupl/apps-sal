import math
n = int(input())

a = 1
for i in reversed(list(range(1, int(math.sqrt(n)) + 1))):
    if n % i == 0:
        a = i
        break
print((a + int(n // a) - 2))
