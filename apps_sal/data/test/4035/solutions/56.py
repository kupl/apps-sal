import math
a, b = list(map(int, input().split()))
ans = -1

for i in range(1010):
    if math.floor(i*0.08) == a and math.floor(i*0.1) == b:
        ans = i
        break

print(ans)

