from collections import deque

n = int(input())
matches = []
for _ in range(n):
    matches.append(list([int(x) - 1 for x in input().split()]))

q = deque(list(range(n)))

days = [0] * n

while q:
    x = q.popleft()
    if len(matches[x]) == 0:
        continue
    y = matches[x][0]
    if matches[y][0] == x:
        day = max(days[x], days[y]) + 1
        days[x] = day
        days[y] = day
        q.append(x)
        q.append(y)
        _ = matches[x].pop(0)
        _ = matches[y].pop(0)

if not any(matches):
    print((max(days)))
else:
    print((-1))
