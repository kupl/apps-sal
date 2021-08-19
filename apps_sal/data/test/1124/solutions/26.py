from math import gcd
N = int(input())
a = list(map(int, input().split()))
count = 0
for A in a:
    count = gcd(count, A)
print(count)
