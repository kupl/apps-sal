import time
(a, b) = (int(i) for i in input().split())
start = time.time()
if a == b:
    print(a)
else:
    print(1)
finish = time.time()
