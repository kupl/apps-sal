import math
(A, B) = map(int, input().split())
ans = math.ceil((B - A) / (A - 1)) + 1
print(ans)
