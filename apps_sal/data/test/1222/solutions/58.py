import queue
k = int(input())
q = queue.Queue()
for i in range(1, 10):
    q.put(i)
lunlun = list(range(1, 10))
cnt = 9

while cnt <= k:
    v = q.get()
    last = v % 10
    if last != 0:
        new = v * 10 + last - 1
        q.put(new)
        lunlun.append(new)
        cnt += 1
    new = v * 10 + last
    q.put(new)
    lunlun.append(new)
    cnt += 1
    if last != 9:
        new = v * 10 + last + 1
        q.put(new)
        lunlun.append(new)
        cnt += 1
print(lunlun[k - 1])
