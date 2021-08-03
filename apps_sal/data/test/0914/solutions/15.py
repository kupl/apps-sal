s = input()
n = int(input())
d = {}
r = 0
for a in s:
    d.setdefault(a, 0)
    d[a] += 1
    if(d[a] > r):
        r = d[a]
if (len(d) > n):
    print(-1)
else:
    l = 0
    while r - l > 1:
        k = (l + r) // 2
        cur = 0
        for x in d.values():
            cur += (x + k - 1) // k
        if cur > n:
            l = k
        else:
            r = k
    print(r)
    s = ''
    for a in d.keys():
        s += a * ((d[a] + r - 1) // r)
    l = len(s)
    s += 'a' * (n - len(s))
    print(s)
