n, l, v1, v2, k = map(int, input().split())
n = (n + k - 1) // k
a = (v2 - v1) / (v1 + v2)
t = l / v2 / (n - (n - 1) * a)
print(n * t + (n - 1) * a * t)
