import bisect, heapq

a, b, c, d, e, f = map(int, input().split())

w = set()
temp = [a * i for i in range((30 - 1) // a + 2)]
for i in temp:
    while i not in w and i <= 30:
        w.add(i)
        i += b
w = list(w)
w.remove(0)
w.sort()

s = set()
temp = [c * i for i in range((3000 - 1) // c + 2)]
for i in temp:
    while i not in s and i <= 3000:
        s.add(i)
        i += d
s = list(s)
s.sort()

queue = []
heapq.heapify(queue)
for i in w:
    if i * 100 > f:
        continue
    num = bisect.bisect(s, i * e)
    for j in range(num - 1, -1, -1):
        if i * 100 + s[j] > f:
            continue
        heapq.heappush(queue, [-s[j] / i, 100 * i + s[j], s[j]])
        break
print(queue[0][1], queue[0][2])
