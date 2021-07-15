def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())

n = ii()
a = li()
b = li()
a.sort()
b.sort()

x = y = 0
for t in range(n):
    if not b:
        x += a.pop()
    elif not a:
        b.pop()
    elif a[-1] > b[-1]:
        x += a.pop()
    else:
        b.pop()

    if not a:
        y += b.pop()
    elif not b:
        a.pop()
    elif b[-1] > a[-1]:
        y += b.pop()
    else:
        a.pop()
print(x - y)

