s, x1, x2 = list(map(int, input().split()))
t1, t2 = list(map(int, input().split()))
p, d = list(map(int, input().split()))
alt = abs(x1 - x2) * t2


curpos = p
curtime = 0
inbus = False
while not (curpos == x2 and inbus):
    if curpos == x1:
        inbus = True
    if curpos == s and d == 1:
        d = -1
    if curpos == 0 and d == -1:
        d = 1
    if d == 1:
        curpos += 1
    else:
        curpos -= 1
    curtime += t1
print(min(curtime, alt))
