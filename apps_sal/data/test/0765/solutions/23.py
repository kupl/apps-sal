
import time
import math

(T, S, q) = (int(i) for i in input().split())
start = time.time()

ans = math.ceil(math.log(T / S, q))
print(ans)
