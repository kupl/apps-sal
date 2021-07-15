enum = int(input())
before = set()
cur = set()
events = [input().split() for i in range(enum)]
for i in range(enum):
    events[i][1] = int(events[i][1])
for i in range(enum):
    if events[i][0] == '-':
        if events[i][1] not in cur:
            before.add(events[i][1])
            cur.add(events[i][1])
        cur.remove(events[i][1])
    else:
        cur.add(events[i][1])

cur = before
max_l = len(cur)
for i in range(enum):
    if events[i][0] == '-':
        cur.remove(events[i][1])
    else:
        cur.add(events[i][1])
    max_l = max(max_l, len(cur))
print(max_l)

