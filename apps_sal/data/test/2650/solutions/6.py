import sys
import heapq as hq
readline = sys.stdin.readline

ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: list(map(int, readline().split()))
nl = lambda: list(map(int, readline().split()))

n, q = nm()
m = 2 * 10**5 + 5
cur = [-1] * n
rate = [0] * n
sec = [list() for _ in range(m)]
for i in range(n):
    a, b = nm()
    rate[i] = a
    cur[i] = b
    hq.heappush(sec[b], (-a, i))
top = list()
for i in range(m):
    if sec[i]:
        hq.heappush(top, (-sec[i][0][0], sec[i][0][1], i))
for _ in range(q):
    c, d = nm()
    c -= 1
    bef = cur[c]
    cur[c] = d
    hq.heappush(sec[d], (-rate[c], c))
    if sec[d][0][1] == c:
        hq.heappush(top, (rate[c], c, d))
    fl = 0
    while sec[bef] and cur[sec[bef][0][1]] != bef:
        hq.heappop(sec[bef])
        fl = 1
    if fl and sec[bef]:
        hq.heappush(top, (-sec[bef][0][0], sec[bef][0][1], bef))
    while not sec[top[0][2]] or sec[top[0][2]][0][1] != top[0][1]:
        hq.heappop(top)
    print((top[0][0]))
