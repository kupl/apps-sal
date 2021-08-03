from math import gcd

n = int(input().strip())
count = 0
for i in range(1, n):
    if gcd(i, n - 1) == 1:
        count += 1
        # print(i)
print(count)
