
import time


(n, k) = (int(i) for i in input().split())

start = time.time()

if (n % k == 0):
    ans = n + k
else:
    ans = (n // k + 1) * k

print(ans)
finish = time.time()
