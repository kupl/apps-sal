_ = int(input())
for __ in [0] * _:
    day = int(input())
    sche = [int(i) for i in input().split()]
    week = sum(sche)
    left = day % week + week
    total = day // week * 7 - 7
    last = sche.index(1)
    s = []
    for i in range(sche.index(1) + 1, 7):
        if sche[i]:
            s.append(i - last - 1)
            last = i
    s.append(7 - sum(s) - len(s) - 1)
    l = len(s)
    total += left
    time = 14
    interval = s + s[:]
    for i in range(l + 1):
        time = min(time, sum(interval[:left - 1]))
        interval.append(interval.pop(0))
    print(total + time)
