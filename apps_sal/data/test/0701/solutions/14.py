s = input()
t = input()
ind = 0
for x in t:
    ind = s.find(x, ind) + 1
    if ind <= 0:
        break
if ind > 0 or len(t) == 0:
    print('automaton')
else:
    ss = list(s)
    tt = list(t)
    bb1 = True
    if len(ss) >= len(tt):
        for x in tt:
            bb = False
            for y in ss:
                if y == x:
                    ss.remove(y)
                    bb = True
                    break
            if not bb:
                bb1 = False
                break
        if bb1:
            if len(s) > len(t):
                print('both')
            else:
                print('array')
        else:
            print('need tree')
    else:
        print('need tree')
