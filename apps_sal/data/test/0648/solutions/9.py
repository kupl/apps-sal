import math

m, bb = [int(item) for item in input().split()]

ans = -1

for a in range(bb + 1):
    b = m * bb - m * a
    ans = max(ans, (a * (a + 1) // 2) * (b + 1) + (b * (b + 1) // 2) * (a + 1))

print(ans)
