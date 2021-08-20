import sys
import heapq
input = sys.stdin.readline
(n, a, b) = map(int, input().split())
if a < b:
    (a, b) = (b, a)
if b == 0:
    print((n - 1) * a)
else:
    remain = n - 1
    ans = 0
    possible = [[a + b, 1]]
    while 1:
        (u, v) = heapq.heappop(possible)
        while possible and possible[0][0] == u:
            v += possible[0][1]
            heapq.heappop(possible)
        if remain <= v:
            ans += u * remain
            break
        ans += u * v
        remain -= v
        heapq.heappush(possible, [u + a, v])
        heapq.heappush(possible, [u + b, v])
    print(ans)
