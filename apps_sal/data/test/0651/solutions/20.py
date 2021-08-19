from itertools import permutations


def ok(n, m, v, a, l):
    x, y = -1, -1
    for i, q in enumerate(v):
        if 'S' in q:
            x = i
            y = q.index('S')
            break
    for i in l:
        if a[i] == 'u':
            x -= 1
        elif a[i] == 'd':
            x += 1
        elif a[i] == 'l':
            y += 1
        elif a[i] == 'r':
            y -= 1

        if x < 0 or x >= n or y < 0 or y >= m or v[x][y] == '#':
            return False

        if v[x][y] == 'E':
            return True

    if x < 0 or x >= n or y < 0 or y >= m or v[x][y] == '#':
        return False

    return v[x][y] == 'E'


n, m = map(int, input().split())

v = [input() for _ in range(n)]

l = list(map(int, input()))

ans = 0

for i in permutations(['u', 'd', 'l', 'r']):
    if ok(n, m, v, i, l):
        ans += 1

print(ans)
