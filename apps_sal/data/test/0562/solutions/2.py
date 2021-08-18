n = int(input())

events = []
for i in range(n):
    a, b = list(map(int, input().split()))
    events.append((a, +1))
    events.append((b, -1))

events = sorted(events, key=lambda x: (x[0], -x[1]))

max_shows = 0
cur_shows = 0

for _, e in events:
    cur_shows += e
    max_shows = max(max_shows, cur_shows)

if max_shows > 2:
    print('NO')
else:
    print('YES')
