import itertools
(n, c) = map(int, input().split())
xvl = []
for _ in range(n):
    (x, v) = map(int, input().split())
    xvl.append((x, v))
get_l = []
sum_v = 0
for (x, v) in xvl:
    sum_v += v
    get_l.append(sum_v - x)
get_l_ac = list(itertools.accumulate(get_l, max))
get_r = []
sum_v = 0
for (x, v) in xvl[::-1]:
    sum_v += v
    get_r.append(sum_v - (c - x))
ans = 0
x = 0
for i in range(n):
    tmp = 0
    if i > 0:
        x = c - xvl[-i][0]
        tmp += get_r[i - 1]
    ans = max(tmp, tmp - x + get_l_ac[n - i - 1], ans)
get_r_ac = list(itertools.accumulate(get_r, max))
x = 0
for i in range(n):
    tmp = 0
    if i > 0:
        x = xvl[i - 1][0]
        tmp += get_l[i - 1]
    ans = max(tmp, tmp - x + get_r_ac[n - i - 1], ans)
print(ans)
