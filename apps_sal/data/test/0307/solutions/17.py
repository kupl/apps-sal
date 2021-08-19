(k2, k3, k5, k6) = list(map(int, input().split()))
k = min(k2, min(k5, k6))
ans = k * 256
k2 -= k
ans += 32 * min(k2, k3)
print(ans)
