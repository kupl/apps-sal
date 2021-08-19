from collections import defaultdict
import heapq
(n, k, q) = map(int, input().split())
a = list(map(int, input().split()))
ok = [0] * n
d = defaultdict(lambda: set())
h = []
for i in range(k - 1):
    heapq.heappush(h, [a[i], i])
    d[a[i]].add(i)
for i in range(k - 1, n):
    heapq.heappush(h, [a[i], i])
    d[a[i]].add(i)
    while h:
        if h[0][1] >= i - k + 1:
            break
        heapq.heappop(h)
    m = list(d[h[0][0]])
    for j in m:
        if j >= i - k + 1:
            ok[j] = 1
        d[h[0][0]].remove(j)
ans = 1145141919810
for i in range(n):
    if ok[i]:
        (s, t) = ([], [])
        for j in range(n):
            if a[i] > a[j]:
                s.sort()
                for l in range(max(0, len(s) - k + 1)):
                    t.append(s[l])
                s = []
            else:
                s.append(a[j])
        s.sort()
        for l in range(max(0, len(s) - k + 1)):
            t.append(s[l])
        t.sort()
        if len(t) >= q:
            ans = min(ans, t[q - 1] - t[0])
print(ans)
