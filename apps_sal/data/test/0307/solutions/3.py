(k2, k3, k5, k6) = map(int, input().split())
n = min(k2, k5, k6)
m = min(k2 - n, k3)
print(n * 256 + m * 32)
