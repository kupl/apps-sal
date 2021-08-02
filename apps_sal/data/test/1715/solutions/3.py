from bisect import bisect
a, b, q = map(int, input().split())
s = sorted([int(input()) for i in range(a)])
t = sorted([int(input()) for i in range(b)])


for i in range(q):
    x = int(input())

    s_i = bisect(s, x)
    d1 = d2 = 10**11
    if s_i < a:
        d1 = s[s_i] - x
        t_i = bisect(t, s[s_i])
        buf = 10**11
        if t_i < b:
            buf = t[t_i] - s[s_i]
        if t_i > 0:
            buf = min(buf, s[s_i] - t[t_i - 1])
        d1 += buf
    if s_i > 0:
        d2 = x - s[s_i - 1]
        t_i = bisect(t, s[s_i - 1])
        buf = 10**11
        if t_i < b:
            buf = t[t_i] - s[s_i - 1]
        if t_i > 0:
            buf = min(buf, s[s_i - 1] - t[t_i - 1])
        d2 += buf

    t_i = bisect(t, x)
    d3 = d4 = 10**11
    if t_i < b:
        d3 = t[t_i] - x
        s_i = bisect(s, t[t_i])
        buf = 10**11
        if s_i < a:
            buf = s[s_i] - t[t_i]
        if s_i > 0:
            buf = min(buf, t[t_i] - s[s_i - 1])
        d3 += buf
    if t_i > 0:
        d4 = x - t[t_i - 1]
        s_i = bisect(s, t[t_i - 1])
        buf = 10**11
        if s_i < a:
            buf = s[s_i] - t[t_i - 1]
        if s_i > 0:
            buf = min(buf, t[t_i - 1] - s[s_i - 1])
        d4 += buf

    print(min(d1, d2, d3, d4))
