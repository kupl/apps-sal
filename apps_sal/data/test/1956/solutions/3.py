import sys

inpy = [int(x) for x in sys.stdin.read().split()]


def win(s, e):
    if e == s:
        return False
    if e == s + 1:
        return True
    if e % 2 == 1:
        if s % 2 == 1:
            return False
        return True
    q = e // 4

    if s <= q:
        return win(s, q)
    q = e // 2
    if(s > q):
        return (e - s) % 2 == 1
    return True


def lose(s, e):
    q = e // 2
    if(s > q):
        return True
    else:
        return win(s, q)


t = inpy[0]
start = (True, False)
inpo = 1
v = (True, True)

for tc in range(t):
    if(inpo + 1 >= len(inpy)):
        print('wtf')
    s, e = inpy[inpo], inpy[inpo + 1]
    inpo = inpo + 2
    v = ((win(s, e), lose(s, e)))
    if start[0] and start[1]:
        break
    if (not start[0]) and (not start[1]):
        break
    if start[1]:
        v = (not v[0], not v[1])
    start = (v[1], v[0])

if((start[0] != True and start[0] != False) or (start[1] != True and start[1] != False)):
    print('wtf')
sw = 2
if start[1]:
    sw = sw - 1
    print(1, end=' ')
else:
    sw = sw - 1
    print(0, end=' ')
if start[0]:
    print(1)
    sw = sw - 1
else:
    print(0)
    sw = sw - 1
if sw:
    print(wtf)
