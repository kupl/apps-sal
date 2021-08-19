import math
n = int(input())
t = math.ceil(math.sqrt(n))
for i in range(t, 1, -1):
    if n % i == 0:
        print(i - 1 + n // i - 1)
        break
else:
    print(n - 1)
