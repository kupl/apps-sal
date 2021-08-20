def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


MAX = 6 * 10 ** 5
n = ii()
a = [input().strip() for i in range(n)]
pos = [[] for i in range(MAX)]
neg = [[] for i in range(MAX)]
for s in a:
    p = m = 0
    for c in s:
        if c == '(':
            p += 1
        else:
            p -= 1
        m = min(m, p)
    if p >= 0:
        pos[p].append(m)
    else:
        neg[-p].append(m)
ans = 0
for p in range(1, MAX):
    c1 = sum((x >= 0 for x in pos[p]))
    c2 = sum((x + p >= 0 for x in neg[p]))
    ans += min(c1, c2)
c3 = sum((x >= 0 for x in pos[0]))
ans += c3 // 2
print(ans)
