x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
n = int(input())
s = list(input())
p = [(0, 0)]
for i in range(n):
    if s[i] == 'U': p.append((p[-1][0], p[-1][1] + 1))
    elif s[i] == 'D': p.append((p[-1][0], p[-1][1] - 1))
    elif s[i] == 'R': p.append((p[-1][0] + 1, p[-1][1]))
    else: p.append((p[-1][0] - 1, p[-1][1]))


def check(m):
    dx, dy = p[-1][0] * (m // n) + p[m % n][0], p[-1][1] * (m // n) + p[m % n][1]
    if abs(x1 + dx - x2) + abs(y1 + dy - y2) <= m:
        return True
    else:
        return False


def outer(k):
    l = 0
    h = 10**10
    ans = -1
    while l <= h:
        m = (l + h) // 2
        if check(n * m + k):
            ans = n * m + k
            h = m - 1
        else:
            l = m + 1
    return ans


a = None
for i in range(n):
    ta = outer(i)
    if ta != -1:
        if a is None:
            a = ta
        else:
            a = min(a, ta)
if a is None: print(-1)
else: print(a)
