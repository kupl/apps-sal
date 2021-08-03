from collections import Counter


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


n = ii()
a1 = [tuple(mi()) for i in range(n)]
a = []
for l, r in a1:
    a.append((l, 0))
    a.append((r, 1))
c = Counter(a)
b = [(k[0], k[1], v) for k, v in c.items()]
b.sort()
ans = [0] * (n + 1)
p = -1
cnt = 0
for x, y, z in b:
    if y == 0:
        ans[cnt] += x - p - 1
        cnt += z
        ans[cnt] += 1
    else:
        if x != p:
            ans[cnt] += x - p
        cnt -= z
    p = x
print(*ans[1:])
