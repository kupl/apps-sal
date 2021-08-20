from collections import deque
(n, k) = map(int, input().split())
q = deque(maxlen=k)
c = list(map(int, input().split()))
for i in c:
    if i not in q:
        q.append(i)
    else:
        continue
print(len(q))
print(*list(q)[::-1])
