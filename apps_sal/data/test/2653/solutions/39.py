import collections

n, q = map(int, input().split())

value = ['-'] * (n + 1)

connected = [set() for i in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    connected[a].add(b)
    connected[b].add(a)

for i in range(q):
    p, x = map(int, input().split())
    if value[p] == '-':
        value[p] = 0
    value[p] -= x

queue = collections.deque(connected[1])

if value[1] == '-':
    value[1] = 0
else:
    value[1] = -value[1]

for i in queue:
    if value[i] == '-':
        value[i] = 0
    else:
        value[i] = -value[i]
    value[i] += value[1]


while queue:
    s = queue.popleft()
    v = value[s]
    for i in connected[s]:
        vi = value[i]
        if vi == '-' or vi < 0:
            if vi == '-':
                vi = 0
            value[i] = -(vi - v)
            queue.append(i)

print(' '.join(str(i) for i in value[1:]))
