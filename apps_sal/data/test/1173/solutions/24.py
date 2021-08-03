from collections import deque
a = int(input())
l = []
for i in range(a):
    tl = list(map(int, input().split()))
    tl = list(map(lambda x: x - 1, tl))
    l.append(tl)

q = deque((range(a)))
days = [0] * a
pairs = [-1] * a
while q:
    x = q.popleft()
    if len(l[x]) == 0:
        continue
    y = l[x].pop(0)
    if pairs[y] == x:
        days[x] = days[y] = max(days[x], days[y]) + 1
        q.append(x)
        q.append(y)
    else:
        pairs[x] = y
if not any(l):
    print(max(days))
else:
    print(-1)
