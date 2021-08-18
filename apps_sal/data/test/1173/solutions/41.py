from collections import deque

n = int(input())
l = [[int(i) - 1 for i in input().split()] for i in range(n)]

q = deque(list(range(n)))
days = [0 for i in range(n)]
pairs = [-1 for i in range(n)]
while q:
    a = q.popleft()
    if len(l[a]) == 0:
        continue
    b = l[a].pop(0)

    if pairs[b] == a:
        days[a] = days[b] = max(days[a], days[b]) + 1
        q.append(a)
        q.append(b)
    else:
        pairs[a] = b
print((max(days) if not any(l) else -1))
