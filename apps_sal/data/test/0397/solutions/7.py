from math import sqrt as sqrt
n, k = map(int, input().split())
t = int(sqrt(8 * n + 8 * k + 9) + 0.0001)
m = (t - 3) // 2
print(n - m)
