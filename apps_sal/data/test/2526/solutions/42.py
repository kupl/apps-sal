from collections import deque
X, Y, A, B, C = list(map(int, input().split()))
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort()
p = p[len(p) - X:]
q.sort()
q = q[len(q) - Y:]
r.sort(reverse=True)
p = deque(p)
q = deque(q)

for i in r:
    if min(p[0], q[0]) > i:
        break
    if p[0] < q[0]:
        p.popleft()
        p.append(i)
    else:
        q.popleft()
        q.append(i)
print((sum(p) + sum(q)))
