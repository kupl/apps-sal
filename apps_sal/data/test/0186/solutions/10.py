
import time


(n, m) = (int(i) for i in input().split())

start = time.time()

h2 = 2 * n
h3 = 3 * m

k = 6
while (k <= min(h2, h3)):
    if h2 + 2 < h3 + 3:
        h2 += 2
    else:
        h3 += 3
    k += 6

print(max(h2, h3))
finish = time.time()
