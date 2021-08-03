import heapq
import sys
def input(): return sys.stdin.readline()


for i in range(int(input())):
    n = int(input())
    s = set()
    h = []
    for i in map(int, input().split()):
        if i % 2 == 0:
            if i in s:
                continue
            s.add(i)
            heapq.heappush(h, -i)
    ans = 0
    while h:
        i = -heapq.heappop(h) // 2
        ans += 1
        if i % 2 == 0:
            if i in s:
                continue
            s.add(i)
            heapq.heappush(h, -i)

    print(ans)
