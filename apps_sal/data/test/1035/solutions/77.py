import math

a, b = map(int, input().split())
x = math.gcd(a, b)
s = [1]
for i in range(2, int(math.sqrt(x) + 1)):
    if x % i == 0:
        while x % i == 0:
            x //= i
        s.append(i)
if x != 1:
    s.append(x)
l = len(s)
print(l)
