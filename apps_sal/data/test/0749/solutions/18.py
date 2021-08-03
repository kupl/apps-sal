s = input()
n = len(s)
l = 0
r = n + 1
while r - l > 1:
    m = (l + r) // 2
    t = set(s[:m])
    d = {}
    for i in range(m):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    for i in range(m, n):
        if s[i] in t:
            d[s[i]] += 1
        if s[i - m] in t:
            d[s[i - m]] -= 1
            if d[s[i - m]] == 0:
                t.remove(s[i - m])
    if len(t) > 0:
        r = m
    else:
        l = m
print(r)
