from math import factorial as f
n = int(input())
ans = f(n) // (n - n // 2) // f(n // 2) // 2 * f(n // 2 - 1)
print(ans)
