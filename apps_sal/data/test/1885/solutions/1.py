from math import factorial
n = int(input())
a = n * (n - 1) * (n - 2) * (n - 3) * (n - 4)
ans = a // factorial(5)
a *= n - 5
ans += a // factorial(6)
a *= n - 6
ans += a // factorial(7)
print(ans)
