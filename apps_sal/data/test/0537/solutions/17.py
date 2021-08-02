import math
n, k = list(map(int, input().split()))
total = n
none = math.ceil(n / 2)
n -= none
index = n // (k + 1)
a = index
b = index * k
none += (n - (a + b))
print(a, b, none)
