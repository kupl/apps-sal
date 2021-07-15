m, n = map(int, input().split())
k_min = 0
g = m // n
s = m - (m // n) * n
k_min = ((g + 1) * g // 2) * s + (g * (g - 1) // 2) * (n - s)
g = m - (n - 1)
k_max = g * (g - 1) // 2
print(k_min, k_max)
