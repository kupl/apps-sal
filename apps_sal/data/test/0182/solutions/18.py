
import time


a = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]

start = time.time()

ans = 0

for i in range(3):
    a[i] -= x[i]
    if a[i] > 0:
        ans += divmod(a[i], 2)[0]
    else:
        ans += a[i]

if ans >= 0:
    print("Yes")
else:
    print("No")

finish = time.time()
