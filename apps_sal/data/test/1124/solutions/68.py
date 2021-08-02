import math
n = int(input())
x = list(map(int, input().split()))
a = 0
for i in range(n):
    a = math.gcd(a, x[i])
print(a)
