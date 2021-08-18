
import time

n = int(input())
m = int(input())
a = []

for i in range(n):
    x = int(input())
    a.append(x)

start = time.time()

a = sorted(a, key=lambda x: -x)
ans = 0

while(m > 0):
    m -= a[ans]
    ans += 1


print(ans)
finish = time.time()
