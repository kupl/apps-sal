import math

n, x, t = map(int, input().split())

time = 0

if n % x == 0:
    time = n / x
else:
    time = math.ceil(n / x)

print(int(t * time))
