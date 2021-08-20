(n, x) = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]
dd = d + d


def b2(k):
    return k * (k + 1) // 2


end_pt = 0
days = 0
best = 0
cur_hugs = b2(dd[0])
while days + dd[end_pt] < x:
    days += dd[end_pt]
    end_pt += 1
    cur_hugs += b2(dd[end_pt])
start_pt = 0
start_day = days + dd[end_pt] - x + 1
while start_day > dd[start_pt]:
    start_day -= dd[start_pt]
    cur_hugs -= b2(dd[start_pt])
    start_pt += 1
cur_hugs -= b2(start_day - 1)
best = cur_hugs
if False:
    print('Initial:')
    print('dd = ', dd)
    print('end_month = ', end_pt)
    print('start_month = ', start_pt)
    print('start_day = ', start_day)
    print('cur_hugs = best = ', best)
while end_pt + 1 < len(dd):
    end_pt += 1
    cur_hugs += b2(dd[end_pt])
    cur_hugs += b2(start_day - 1)
    start_day += dd[end_pt]
    while start_day > dd[start_pt]:
        start_day -= dd[start_pt]
        cur_hugs -= b2(dd[start_pt])
        start_pt += 1
    cur_hugs -= b2(start_day - 1)
    best = max(best, cur_hugs)
print(best)
