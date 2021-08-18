import collections

n, m = map(int, input().split())
a = list(map(int, input().split()))
md = n // m
c = [[] for _ in range(m)]
mx, ind, moves = (0,) * 3
movable = collections.deque()
change = []

for i in range(n):
    c[a[i] % m].append(i)

for i in range(m):
    req = md - len(c[i])
    if req <= 0:
        for j in range(-req):
            movable.append(i)
    else:
        while req > 0:
            if len(movable) == 0:
                change.append([i, req])
                break
            old = movable[0]
            add = i - old
            a[c[old][-1]] += add
            moves += add

            c[i].append(c[old][-1])
            del c[old][-1]
            movable.popleft()
            req -= 1

for obj in change:
    i, req = obj[0], obj[1]
    while req > 0:
        old = movable[0]
        add = i + m - old
        a[c[old][-1]] += add
        moves += add

        c[i].append(c[old][-1])
        del c[old][-1]
        movable.popleft()
        req -= 1

ans = [0 for _ in range(n)]

for i in range(m):
    for j in range(md):
        ans[c[i][j]] = a[c[i][j]]

print(moves)
print(*ans)
