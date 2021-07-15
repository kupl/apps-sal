from math import sqrt
n = int(input())
i = int(sqrt(n) + 1)
while n % i > 0:
    i -= 1
j = n // i
ans = i + j - 2
print(ans)

