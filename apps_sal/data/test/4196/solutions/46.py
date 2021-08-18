import math

n = int(input())
a = list(map(int, input().split()))

lefGcd = [0] * 100100
rigGcd = [0] * 100100

lefGcd[0] = a[0]
rigGcd[n - 1] = a[n - 1]

for i in range(1, n):
    lefGcd[i] = math.gcd(lefGcd[i - 1], a[i])

for i in reversed(list(range(0, n - 1))):
    rigGcd[i] = math.gcd(rigGcd[i + 1], a[i])

ans = max(rigGcd[1], lefGcd[n - 2])

for i in range(1, n - 1):
    ans = max(ans, math.gcd(lefGcd[i - 1], rigGcd[i + 1]))

print(ans)
