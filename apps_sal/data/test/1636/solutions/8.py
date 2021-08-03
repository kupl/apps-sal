from sys import stdin
_data = iter(stdin.read().split('\n'))
def input(): return next(_data)


n = int(input())
ref, front = {}, {}
ans = []
max_x, max_y = 0, 0
for _ in range(n):
    x, y = list(map(int, input().split()))
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    ref[(x, y)] = 2
    if x == 0:
        ref[(x, y)] -= 1
    if y == 0:
        ref[(x, y)] -= 1
    if (x, y) == (0, 0):
        del ref[(x, y)]
        front[y - x] = x, y
ws = list(map(int, input().split()))
for w in ws:
    if w not in front:
        ans = []
        break
    x, y = front.pop(w)
    ans.append((x, y))
    for dx, dy in ((1, 0), (0, 1)):
        nx, ny = x + dx, y + dy
        if (nx, ny) not in ref:
            continue
        ref[(nx, ny)] -= 1
        if ref[(nx, ny)] == 0:
            del ref[(nx, ny)]
            front[ny - nx] = (nx, ny)
if ans:
    print('YES')
    print('\n'.join('{} {}'.format(x, y) for x, y in ans))
else:
    print('NO')
