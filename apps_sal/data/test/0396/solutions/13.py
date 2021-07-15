from collections import deque
q = deque()
l, r = list(map(int, input().split()))
q.append(1);
u = 1
p = 0
if l <= 1:
    p += 1
while u <= r*r:
    u = q.popleft()
    if q.count(u * 2) == 0:
        q.append(u * 2)
        if u * 2 >= l and u * 2 <= r:
            p += 1
    if q.count(u * 3) == 0:
        q.append(u * 3)
        if u * 3 >= l and u * 3 <= r:
            p += 1
print(p)

