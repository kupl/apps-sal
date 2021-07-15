import math

n = int(input())
common = 1
for num in range(1,n + 1):
    common = common * num // math.gcd(common, num)
print(common + 1)
