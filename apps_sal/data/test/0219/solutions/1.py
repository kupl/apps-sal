n, m, s, d = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
if a[0] - 1 < s:
    print('IMPOSSIBLE')
    return
strategy = []
i = 0
stand_point = 0
while i < n:
    strategy.append(a[i] - stand_point - 1)
    stand_point = a[i] - 1
    j = i + 1
    if j != n:
        a2, a1 = a[j], a[i]
    while j < n:
        if a2 - a1 - 2 < s:
            if a2 - a[i] + 2 > d:
                print('IMPOSSIBLE')
                return
            j += 1
            if j != n:
                a1 = a2
                a2 = a[j]
            continue
        else:
            strategy.append(a1 - a[i] + 2)
            i = j
            stand_point = a[i - 1] + 1
            break
    else:
        #print(stand_point, strategy_run, strategy_jump)
        if d >= a[-1] - stand_point + 1 and strategy[-1] >= s:
            strategy.append(a[-1] - stand_point + 1)
        else:
            print('IMPOSSIBLE')
            return
        i = j
        stand_point = a[i - 1] + 1

if m - stand_point != 0:
    strategy.append(m - stand_point)
turn_flag = True
for i in strategy:
    if turn_flag:
        print('RUN', i)
    else:
        print('JUMP', i)
    turn_flag = not turn_flag

