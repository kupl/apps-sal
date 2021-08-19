import math
n = int(input())
p10 = int(math.log10(n + 1))
p = pow(10, p10)
years = (int(n / p) + 1) * p - n
print(years)
