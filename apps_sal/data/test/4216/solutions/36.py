import math
n = int(input())

for a in range(1, int(math.sqrt(n)) + 1):
    if n % a == 0:
        b = n // a
        ans = len(str(b))
print(ans)
