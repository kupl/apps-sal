from math import factorial as f
n = int(input())
res = 0
for i in range(5, 8):
    res += f(n) // (f(n - i) * f(i))
print(res)
