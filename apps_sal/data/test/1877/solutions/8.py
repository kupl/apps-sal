def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


n = ii()
S = input().strip()
x = y = c = 0
k = None
for s in S:
    if s == 'U':
        y += 1
    else:
        x += 1
    if y > x:
        if k == 'D':
            c += 1
        k = 'U'
    elif x > y:
        if k == 'U':
            c += 1
        k = 'D'

print(c)
