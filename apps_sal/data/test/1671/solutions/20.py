
import time

n = int(input())
m = [int(i) for i in input().split()]

start = time.time()

s = divmod(sum(m), n)[0]

a1 = 0
a2 = 0

for i in m:
    if i < s:
        a1 += s - i

    if i > s + 1:
        a2 += i - s - 1
print(max(a1, a2))
finish = time.time()
