
import time

n = int(input())
A = [int(i) for i in input().split()]

start = time.time()

l0 = A[0]
l = A[0]
A = A[1:]
m = max(A)

while l <= m:
    l += 1
    A[A.index(m)] -= 1
    m = max(A)

print(l - l0)
finish = time.time()
