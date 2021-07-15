from math import sqrt

n = int(input())

for i in range(int(sqrt(n) + 1)):
    if i ** 2 <= n:
        ans = i ** 2
print(ans)
