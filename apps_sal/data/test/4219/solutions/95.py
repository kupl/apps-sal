N = int(input())
xy = [[] for _ in range(N)]
for i in range(N):
    a = int(input())
    for _ in range(a):
        (x, y) = map(int, input().split())
        x -= 1
        xy[i].append((x, y))
ans = 0
s = set()
t = set()


def true(s, t, j):
    if j not in t:
        s.add(j)
        return False
    return True


def false(s, t, j):
    if j not in s:
        t.add(j)
        return False
    return True


def chk(i):
    s = set()
    t = set()
    fl = False
    for j in range(N):
        if i >> j & 1:
            fl |= true(s, t, j)
            for (x, y) in xy[j]:
                fl |= true(s, t, x) if y == 1 else false(s, t, x)
        else:
            fl |= false(s, t, j)
    return fl


ans = 0
for i in range(2 ** N):
    if chk(i):
        continue
    cnt = 0
    for j in range(N):
        if i >> j & 1:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
