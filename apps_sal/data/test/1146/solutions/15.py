
import time


(n, m) = (int(i) for i in input().split())

a = [0 for i in range(m)]

for i in range(n):
    b = [int(i) for i in input().split()]
    for j in b[1:]:
        a[j - 1] = 1

start = time.time()

if 0 in a:
    print('NO')
else:
    print('YES')

finish = time.time()
