import bisect
(a, b, q) = list(map(int, input().split()))
s = [-10 ** 19]
for i in range(a):
    s.append(int(input()))
s.append(10 ** 19)
t = [-10 ** 19]
for i in range(b):
    t.append(int(input()))
t.append(10 ** 19)
for i in range(q):
    x = int(input())
    ps = bisect.bisect_right(s, x)
    pt = bisect.bisect_right(t, x)
    ret = 10 ** 19
    for loc1 in (s[ps], s[ps - 1]):
        for loc2 in (t[pt], t[pt - 1]):
            val = min(abs(x - loc1) + abs(loc1 - loc2), abs(x - loc2) + abs(loc1 - loc2))
            ret = min(ret, val)
    print(ret)
