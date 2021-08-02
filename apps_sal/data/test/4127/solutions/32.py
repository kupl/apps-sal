import math
A, B = map(float, input().split())
B = B * 100
ans = int(A) * round(B) // 100
print(ans)
