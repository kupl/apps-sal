from math import ceil


def point(x, y, r, s, p):
    if y == 'r':
        y = p
    if y == 's':
        y = r
    if y == 'p':
        y = s
    return ceil(x / 2) * y


n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())
ans = 0
for _ in range(k):
    l = t[_::k]
    x = 1
    y = l[0]
    for i in l[1:]:
        if i != y:
            ans += point(x, y, r, s, p)
            x = 1
            y = i
        else:
            x += 1
    ans += point(x, y, r, s, p)
print(ans)
