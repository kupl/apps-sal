import time
(a, b) = (int(i) for i in input().split())
start = time.time()
m = min(a, b)
a = divmod(a - m, 2)[0]
b = divmod(b - m, 2)[0]
print(m, a + b)
finish = time.time()
