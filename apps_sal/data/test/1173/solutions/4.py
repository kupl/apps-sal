from collections import deque

n = int(input())
a = []
for i in range(n):
    ai = list(map(int, input().split()))
    a.append([tuple(sorted((i, aij - 1))) for aij in ai])

idx = [0] * (n + 1)
pool = set()
q = deque([ai[0] for ai in a])
day = 1
s = set()

while q:
    # print('-' * 30)
    # print('pool:', pool)
    # print('s:', s)
    # print('q:', q)
    p = q.popleft()
    if p not in pool:
        pool.add(p)
    else:
        pool.remove(p)
        x, y = p
        idx[x] += 1
        idx[y] += 1

        if x in s or y in s:
            day += 1
            s = {x, y}
        else:
            s.add(x)
            s.add(y)

        if idx[x] < n - 1:
            q.append(a[x][idx[x]])
        if idx[y] < n - 1:
            q.append(a[y][idx[y]])

# print('=' * 20)
if pool:
    print(-1)
else:
    print(day)
