def process(a):
    assert len(a) >= 2
    n = len(a)
    min_ = float('inf')
    for (i, [cnt, c]) in enumerate(a):
        if i == 0 or i == n - 1:
            min_ = min(min_, cnt)
        else:
            min_ = min(min_, (cnt + 1) // 2)
    b = []
    for (i, [cnt, c]) in enumerate(a):
        if i == 0 or i == n - 1:
            remain = cnt - min_
        else:
            remain = cnt - min_ * 2
        if remain <= 0:
            continue
        if len(b) == 0 or c != b[-1][1]:
            b.append([remain, c])
        else:
            (pre_cnt, pre_c) = b.pop()
            b.append([pre_cnt + remain, c])
    return (b, min_)


S = input() + ' '
cur = []
cnt = 0
pre = ''
for x in S:
    if cnt == 0:
        cnt += 1
        pre = x
    elif x != pre:
        cur.append([cnt, pre])
        cnt = 1
        pre = x
    else:
        cnt += 1
cnt = 0
while len(cur) not in [0, 1]:
    (cur, min_) = process(cur)
    cnt += min_
print(cnt)
