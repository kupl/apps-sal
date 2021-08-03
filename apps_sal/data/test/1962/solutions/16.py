import bisect
import sys
n, k, l = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
li = bisect.bisect_right(a, a[0] + l) - 1
# print(li)
if li + 1 < n:
    print(0)
    return
b = [False] * (n * k)
m = 0
i = 0
t = 0
while i <= li:
    m = m + a[i]
    t += 1
    b[i] = True
    i = i + k
    # print(a[i],i)
i = li
while t < n:
    if b[i] == False:
        m = m + a[i]
        t += 1
    i -= 1
print(m)
