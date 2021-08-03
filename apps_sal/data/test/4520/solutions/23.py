import heapq as h
n, k = list(map(int, input().split()))
l = [0] * n
r = [0] * n
events = [(0, 0)] * 2 * n
for i in range(n):
    l[i], r[i] = list(map(int, input().split()))
    events[2 * i] = (l[i], 0, i)
    events[2 * i + 1] = (r[i], 1, i)
events.sort()
s = []
ans = []
for e in events:
    x, t, id = e
    if t == 0:
        h.heappush(s, (-r[id], l[id], id))
    else:
        temp = []
        while s:
            x = h.heappop(s)
            if x == (-r[id], l[id], id):
                break
            temp.append(x)
        for x in temp:
            h.heappush(s, x)
    while len(s) > k:
        x = h.heappop(s)
        ans.append(x[2])
print(len(ans))
print(*[x + 1 for x in ans])
