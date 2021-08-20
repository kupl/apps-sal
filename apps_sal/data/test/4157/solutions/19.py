from heapq import heappop, heappush
n = int(input())
a = []
c = input().split()
for i in c:
    i = int(i)
    p = 0
    while not i % 3:
        i //= 3
        p += 1
    a += [[] for j in range(p - len(a) + 1)]
    heappush(a[p], i * 3 ** p)
o = ''
n = len(a)
for i in range(1, n + 1):
    while a[n - i]:
        o += str(heappop(a[n - i])) + ' '
print(o)
