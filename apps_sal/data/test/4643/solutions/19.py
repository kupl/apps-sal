import time
start_ = time.time()
(n, *a) = input().split()
a = list(map(int, a))
print(' '.join((str(ch) for ch in sorted(a))))
while True:
    if time.time() - start_ > 1.7:
        break
