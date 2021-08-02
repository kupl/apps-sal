from math import gcd

n = int(input())

sum = 1

for i in range(2, n + 1):
    sum = (sum * i) // gcd(sum, i)

print(sum + 1)
