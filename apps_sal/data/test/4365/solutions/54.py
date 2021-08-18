import math
K = int(input())
if K % 2:
    ans = (K // 2 + 1) * (K // 2)
else:
    ans = (K // 2) * (K // 2)
pass
print(ans)
