from bisect import *
(a, b, q) = map(int, input().split())
s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]
inf = 10 ** 18
s = [-inf] + s + [inf]
t = [-inf] + t + [inf]
for i in range(q):
    x = int(input())
    s_ind = bisect_left(s, x)
    t_ind = bisect_left(t, x)
    res = inf
    for cand_s in [s[s_ind - 1], s[s_ind]]:
        for cand_t in [t[t_ind - 1], t[t_ind]]:
            st = abs(cand_s - cand_t)
            dx = min(abs(cand_s - x), abs(cand_t - x))
            res = min(res, st + dx)
    print(res)
