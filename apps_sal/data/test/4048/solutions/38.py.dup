import math
N = int(input())
a = 0
for i in range(1, int(math.sqrt(N) // 1) + 1):
    a = max(a, math.gcd(N, i))
print(a + N // a - 2)
