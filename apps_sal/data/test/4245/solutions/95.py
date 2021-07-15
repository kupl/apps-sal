A, B = map(int, input().split())
import math
ans = math.ceil((B - A) / (A - 1)) + 1
print(ans)
