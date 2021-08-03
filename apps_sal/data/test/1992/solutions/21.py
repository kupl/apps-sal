n, m, k = (int(x) for x in input().split())
a = [int(x) for x in input().split()]
forward = dict(enumerate(a))
backward = dict((y, x) for (x, y) in enumerate(a))
b = [int(x) for x in input().split()]
res = 0
for x in b:
    pos = backward[x]
    res += pos // k + 1
    if pos != 0:
        prev = forward[pos - 1]
        forward[pos] = prev
        forward[pos - 1] = x
        backward[prev] = pos
        backward[x] = pos - 1
print(res)
