def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


n = ii()
s = input().strip()
g = []
i = 0
lng = 0
while i < n:
    if s[i] == 'S':
        i += 1
        continue
    j = i + 1
    while j < n and s[j] == 'G':
        j += 1
    g.append((i, j))
    lng = max(lng, j - i)
    i = j + 1
if not g:
    ans = 0
elif len(g) == 1:
    ans = lng
else:
    extra = len(g) > 2
    ans = lng + 1
    for i in range(len(g) - 1):
        (s, e) = g[i]
        (s2, e2) = g[i + 1]
        if s2 != e + 1:
            continue
        ans = max(ans, e - s + e2 - s2 + extra)
print(ans)
