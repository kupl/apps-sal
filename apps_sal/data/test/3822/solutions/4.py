n, l, v1, v2, k = list(map(int, input().split()))
m = (n - 1) // k + 1
v = v1 + v2
x = l * v * v2 / (m * v * v2 - (m - 1) * (v2 - v1) * v2)
print(x / v2 + (l - x) / v1)
