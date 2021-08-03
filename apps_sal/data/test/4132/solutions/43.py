import math
N = int(input())
a = list(map(int, input().split()))
b = math.gcd(a[0], a[1])
for i in range(N - 1):
    b = math.gcd(a[i + 1], b)
print(b)
