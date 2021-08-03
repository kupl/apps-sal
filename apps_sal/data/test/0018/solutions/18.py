s = input()
n = len(s)
cur = ('z', n)
mi = [cur for _ in range(n)]
ns = ['z'] * n
for i in range(n - 1, -1, -1):
    if (s[i], i) < cur:
        cur = (s[i], i)
    mi[i] = cur
    ns[i] = s[i]
pos = 0
cache = list()
res = ''

while len(res) < n:
    c, i = mi[pos]
    res += c
    cache += ns[pos:i]
    pos = i
    if cache:
        val = cache[-1]
        mi[pos] = (val, pos)
        ns[pos] = val
        if pos < n - 1:
            mi[pos] = min(mi[pos], mi[pos + 1])
        cache.pop()
    else:
        pos += 1


print(res)
