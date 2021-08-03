import math
n, x = map(int, input().split())
al = list(map(int, input().split()))


temp = abs(x - al[0])

for i in range(1, n):
    y = al[i] - al[i - 1]
    temp = math.gcd(temp, y)

print(temp)
