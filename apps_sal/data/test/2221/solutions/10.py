(x1, y1) = [int(i) for i in input().split()]
(x2, y2) = [int(i) for i in input().split()]
n = int(input())
s = input()


def dst(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


d = dst(x1, y1, x2, y2)
dx = dy = 0
ss = []
for i in range(n):
    if s[i] == 'U':
        dy += 1
    elif s[i] == 'D':
        dy -= 1
    elif s[i] == 'R':
        dx += 1
    else:
        dx -= 1
    ss.append((dx, dy))
l = 1
r = 10 ** 18


def check(m):
    c = m // n
    x = x1 + dx * c
    y = y1 + dy * c
    r = m % n
    if r != 0:
        x += ss[r - 1][0]
        y += ss[r - 1][1]
    d = dst(x2, y2, x, y)
    if d <= m:
        return True
    return False


ans = 10 ** 19
while r >= l:
    m = int((r + l) // 2)
    if check(m):
        ans = min(ans, m)
        r = m - 1
    else:
        l = m + 1
if ans == 10 ** 19:
    print(-1)
else:
    print(ans)
