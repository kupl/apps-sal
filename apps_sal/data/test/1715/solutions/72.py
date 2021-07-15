import bisect
a, b, q = map(int, input().split())
ss = [int(input()) for _ in range(a)]
ts = [int(input()) for _ in range(b)]
xs = [int(input()) for _ in range(q)]
ss = [-float('inf')] + ss + [float('inf')]
ts = [-float('inf')] + ts + [float('inf')]
for x in xs:
    s_r = bisect.bisect_left(ss, x)
    t_r = bisect.bisect_left(ts, x)
    s_l = s_r - 1
    t_l = t_r - 1
    res = float('inf')
    if ss[s_l] > ts[t_l]:
        res = min(res, x - ts[t_l], (x - ss[s_l])*2 + (ts[t_r] - x))
    elif ss[s_l] < ts[t_l]:
        res = min(res, x - ss[s_l], (x - ts[t_l])*2 + (ss[s_r] - x))
    else:
        res = min(res, (x - ss[s_l])*2 + (ss[s_r] - x), x - ss[s_l]*2 + (ts[t_r] - x))
    if ss[s_r] > ts[t_r]:
        res = min(res, ss[s_r] - x, (ts[t_r] - x)*2 + (x - ss[s_l]))
    elif ss[s_r] < ts[t_r]:
        res = min(res, ts[t_r] - x, (ss[s_r] - x)*2 + (x - ts[t_l]))
    else:
        res = min(res, (ss[s_r] - x)*2 + (x - ss[s_l]), (ss[s_r] - x)*2 + (x - ts[t_l]))
    print(res)
