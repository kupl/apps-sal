from queue import Queue
s = input().strip()
t = [[] for i in range(10)]
for a in range(len(s)):
    b = int(s[a])
    t[b].append(a)
d = [-1] * len(s)
d[0] = 0
q = Queue()
q.put(0)
while q.empty() == False:
    if d[len(s) - 1] != -1:
        break
    h = q.get(0)
    value = int(s[h])
    for c in t[value]:
        if d[c] == -1:
            d[c] = d[h] + 1
            q.put(c)
    t[value] = []
    if h + 1 < len(s) and d[h + 1] == -1:
        d[h + 1] = d[h] + 1
        q.put(h + 1)
    if h - 1 > 0 and d[h - 1] == -1:
        d[h - 1] = d[h] + 1
        q.put(h - 1)
print(d[len(s) - 1])
