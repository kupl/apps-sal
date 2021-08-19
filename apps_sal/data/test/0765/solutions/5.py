import time
import math
(T, S, q) = (int(i) for i in input().split())
start = time.time()
ans = math.log(T / S, q)
if int(ans) - ans != 0:
    ans = int(ans) + 1
else:
    ans = int(ans)
print(ans)
finish = time.time()
