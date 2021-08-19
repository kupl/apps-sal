from collections import Counter
import heapq
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    rep = Counter()
    ans = 0
    heap = []
    for i in range(len(a)):
        rep[a[i]] += 1
        if rep[a[i]] == 1:
            heapq.heappush(heap, -a[i])
    while heap:
        x = -heapq.heappop(heap)
        if x % 2 == 0:
            dx = x // 2
            if rep[dx] == 0:
                heapq.heappush(heap, -dx)
                rep[dx] = 1
            else:
                rep[dx] += rep[x]
            ans += 1
    print(ans)
