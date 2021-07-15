from collections import deque
ds = ((1, 0), (0, 1), (-1, 0), (0, -1))
n, m = list(map(int, input().split()))
a = [list(input()) for _ in range(n)]
si, sj = tuple(map(int, input().split()))
ti, tj = tuple(map(int, input().split()))
si -= 1
sj -= 1
ti -= 1
tj -= 1

def count_ok(i, j):
    r = 0
    for di, dj in ds:
        ni, nj = i + di, j + dj
        if (0 <= ni < n and 0 <= nj < m and a[ni][nj] != 'X') \
           or (ni, nj) == (si, sj):
            r += 1
    return r

if (si, sj) == (ti, tj):
    print('YES' if count_ok(si, sj) >= 1 else 'NO')
    return

c = a[ti][tj]
a[ti][tj] = '.'
used = set()
q = deque()
used.add((si, sj))
q.append((si, sj))
while q:
    i, j = q.popleft()
    for di, dj in ds:
        ni, nj = i + di, j + dj
        if 0 <= ni  < n and 0 <= nj < m and\
           a[ni][nj] != 'X' and (ni, nj) not in used:
            used.add((ni, nj))
            q.append((ni, nj))
if (ti, tj) not in used:
    print('NO')
else:
    if c == 'X':
        print('YES')
    else:
        print('YES' if count_ok(ti, tj) >= 2 else 'NO')

          
        

