def check(length: int):
    nonlocal n, x, y, cur, hor, ver
    hor = 0
    ver = 0
    for i in range(length, n):
        upd(i)
    for i in range(n - length + 1):
        if abs(x - hor) + abs(y - ver) <= length:
            return True
        if i + length < n:
            upd(i)
            minus_upd(i + length)
    return False


def upd(pos: int):
    nonlocal s, ver, hor
    if s[pos] == 'U':
        ver += 1
    elif s[pos] == 'D':
        ver -= 1
    elif s[pos] == 'R':
        hor += 1
    else:
        hor -= 1


def minus_upd(pos: int):
    nonlocal s, ver, hor
    if s[pos] == 'U':
        ver -= 1
    elif s[pos] == 'D':
        ver += 1
    elif s[pos] == 'R':
        hor -= 1
    else:
        hor += 1


n = int(input())
s = list(input())
x, y = map(int, input().split())
if (x + y) % 2 != n % 2 or abs(x) + abs(y) > n:
    print(-1)
    return

ver = 0
hor = 0
cur = 0
for i in range(n):
    upd(i)

left = -1
r = n
while r - left > 1:
    length = (r + left) // 2
    if check(length):
        r = length
    else:
        left = length

print(r)
