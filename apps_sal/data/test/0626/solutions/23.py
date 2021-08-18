
import time

n = int(input())
A = [int(i) for i in input().split()]

start = time.time()

t = 0
now = 0
ans = -1

while(t < n):
    ans += 1
    for i in range(n):
        if A[i] >= 0 and A[i] <= t:
            t += 1
            A[i] = -1
    if (t == n):
        break
    ans += 1
    for i in range(n):
        if A[n - 1 - i] >= 0 and A[n - 1 - i] <= t:
            t += 1
            A[n - 1 - i] = -1

print(ans)
finish = time.time()
