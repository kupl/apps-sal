import math
n = int(input())
a = math.gcd(n, 2)  # 最大公約数
print(n * 2 // a)
