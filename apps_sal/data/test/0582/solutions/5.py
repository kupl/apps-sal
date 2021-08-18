import heapq
import sys
input = sys.stdin.readline
h = []
n = int(input())
a = [int(x) for x in input().strip().split()]
t = [int(x) for x in input().strip().split()]
for i in range(len(t)):
    a[i] = [a[i], t[i]]
a.sort(key=lambda x: (x[0], -x[1]))
prev, i, ans = a[0][0], 1, 0
while(i < len(a)):
    if h:
        if a[i][0] == prev:
            heapq.heappush(h, [-a[i][1], a[i][0]])
            i += 1
        elif a[i][0] == prev + 1:
            heapq.heappush(h, [-a[i][1], a[i][0]])
            p = heapq.heappop(h)
            ans += (-p[0] * (prev + 1 - p[1]))
            prev = prev + 1
            i += 1
        else:
            p = heapq.heappop(h)
            ans += (-p[0] * (prev + 1 - p[1]))
            prev = prev + 1
    else:
        if a[i][0] != prev:
            prev = a[i][0]
            i += 1
        else:
            heapq.heappush(h, [-a[i][1], a[i][0]])
            i += 1
while h:
    p = heapq.heappop(h)
    ans += (-p[0] * (prev + 1 - p[1]))
    prev = prev + 1
print(ans)
