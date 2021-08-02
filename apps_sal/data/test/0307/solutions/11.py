k2, k3, k5, k6 = map(int, input().split())
s = min(k2, k5, k6) * 256
k2 = k2 - min(k2, k5, k6)
print(s + min(k2, k3) * 32)
