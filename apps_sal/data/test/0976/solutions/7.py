import sys
(n, x) = (int(x) for x in input().split(' '))
cur = 1
count = 0
for i in range(0, n):
    (l, r) = (int(x) for x in input().split(' '))
    while cur + x <= l:
        cur += x
    count += r - cur + 1
    cur = r + 1
print(count)
