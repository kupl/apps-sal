s = input()
g = 'aouien'
g1 = 'aouie'
state = 0
ok = True
for el in s:
    if state == 0:
        if el in g:
            state = 0
        else:
            state = 1
    else:
        if el not in g1:
            ok = False
        state = 0
if state == 1:
    ok = False
if ok:
    print("YES")
else:
    print("NO")
