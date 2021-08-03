from collections import deque
N, K = map(int, input().split())
id_list = list(map(int, input().split()))


que = deque()
used = set()

for id in id_list:
    if id in used:
        continue
    else:
        if len(que) >= K:
            q = que.pop()
            used.remove(q)
        que.appendleft(id)
        used.add(id)

print(len(que))
while len(que) != 0:
    print(que.popleft(), end=" ")
