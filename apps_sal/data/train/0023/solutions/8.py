import heapq as hq
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    vt = [list(map(int, input().split())) for i in range(n)]
    vt.sort(reverse=True)
    q = []
    hq.heapify(q)
    ans = 0
    cnt = 0
    for i in range(n):
        hq.heappush(q, vt[i][1])
        if vt[i][0] >= n - i + cnt:
            ans += hq.heappop(q)
            cnt += 1
    print(ans)
