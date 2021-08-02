n = int(input())
s = input()
ans = 0
for i in range(1, n - 1):
    a = set(s[:i])
    b = set(s[i:])
    q = max(len(a), len(b))
    t = 0
    if ans >= q:
        continue
    if len(a) >= len(b):
        w = list(a)
        h = list(b)
    else:
        w = list(b)
        h = list(a)
    for k in range(q):
        if w[k] in h:
            t += 1
    ans = max(ans, t)
print(ans)
