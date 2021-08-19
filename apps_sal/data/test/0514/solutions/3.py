from math import ceil
test = int(input())
for z in range(test):
    (day, work) = list(map(int, input().split()))
    l = -1
    r = day
    while r - l > 1:
        m = (l + r) // 2
        new_work = ceil(work / (m + 1))
        if new_work + m <= day:
            r = m
        else:
            l = m
    if r + ceil(work / (r + 1)) <= day:
        print('YES')
    else:
        print('NO')
