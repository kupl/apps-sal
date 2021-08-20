(k2, k3, k5, k6) = list(map(int, input().split()))
n = min(k2, k5, k6)
s = n * 256
k2 -= n
if k2 > 0:
    s += min(k2, k3) * 32
print(s)
