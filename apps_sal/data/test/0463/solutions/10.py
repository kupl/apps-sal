can11 = set()
can12 = set()
can2 = False
(n, x) = list(map(int, input().split()))
a = list(map(int, input().split()))
for ai in a:
    if ai in can11:
        print('0')
        break
    can11.add(ai)
    ai2 = ai & x
    if ai2 == ai:
        continue
    if ai2 in can12:
        can2 = True
    else:
        can12.add(ai2)
else:
    can11.intersection_update(can12)
    if can11:
        print(1)
    elif can2:
        print(2)
    else:
        print('-1')
