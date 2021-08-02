k2, k3, k5, k6 = list(map(int, input().split()))

s = min(k2, k5, k6) * 256
k2 -= min(k2, k5, k6)
s += min(k2, k3) * 32

print(s)
