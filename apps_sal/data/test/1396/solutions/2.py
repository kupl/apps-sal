n, k, x = list(map(int, input().split()))


def lr_bound(c, i, x):
    l = i
    r = i

    while l > 0 and c[l - 1] == x:
        l -= 1
    while r < len(c) - 1 and c[r + 1] == x:
        r += 1
    return l, r


def destroy(c, i, x):
    c = c[:]
    c.insert(i, x)

    dest = 0
    while len(c) > 2:
        if i >= len(c):
            i = len(c) - 1
        if i < 0:
            i = 0
        l, r = lr_bound(c, i, c[i])
        if r - l >= 2:
            c[l:r + 1] = []
            dest += (r - l) + 1
            i = l
        else:
            break
    return dest - 1


c = list(map(int, input().split()))

scores = []
for i in range(len(c)):
    scores.append(destroy(c, i, x))

print(max([0] + scores))
