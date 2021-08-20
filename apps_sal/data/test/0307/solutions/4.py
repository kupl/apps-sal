(k2, k3, k5, k6) = list(map(int, input().split()))
mn_56 = min(k5, k6)
mn_256 = min(mn_56, k2)
rest_k2 = k2 - mn_256
k32 = min(k3, rest_k2)
print(mn_256 * 256 + k32 * 32)
