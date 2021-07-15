import math

a, b = list(map(int, input().split()))
ans = -1
for i in range(math.ceil(a / 0.08), math.floor((a + 1) / 0.08) + 1):
    if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
        ans = i
        break
print(ans)

