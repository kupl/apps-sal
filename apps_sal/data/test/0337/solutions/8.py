def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


w, h = mi()
u1, d1 = mi()
u2, d2 = mi()
c = w
for i in range(h, -1, -1):
    c += i
    if i == d1:
        c -= u1
    elif i == d2:
        c -= u2
    c = max(0, c)
print(c)
