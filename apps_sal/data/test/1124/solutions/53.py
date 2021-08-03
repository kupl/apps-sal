import math
input()
a = 0
for i in map(int, input().split()):
    a = math.gcd(a, i)
print(a)
