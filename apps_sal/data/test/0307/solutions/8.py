k2, k3, k5, k6 = map(int, input().split(' '))
num256 = min(k2, k5, k6)
ans = 256 * num256
k2 -= num256
num32 = min(k2, k3)
ans += 32 * num32
print(ans)
