from collections import deque

N = int(input())
L = [deque([int(i)-1 for i in input().split()]) for i in range(N)]

q = deque(list(range(N)))
d = [0 for i in range(N)]
pairs = [-1 for i in range(N)]
while q:
    a = q.popleft()  # qの左端の選手のindexをpopleft
    if len(L[a]) == 0:
        continue
    b = L[a].popleft()

    if pairs[b] == a:  # bのリクエストがaなら
        d[a] = d[b] = max(d[a], d[b]) + 1
        q.append(a)
        q.append(b)
    else:
        pairs[a] = b
print((max(d) if not any(L) else -1))

