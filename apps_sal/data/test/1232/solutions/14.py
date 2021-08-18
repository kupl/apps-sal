
import time


(na, nb) = (int(i) for i in input().split())
(k, m) = (int(i) for i in input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

start = time.time()

if A[k - 1] < B[len(B) - m]:
    print('YES')
else:
    print('NO')

finish = time.time()
