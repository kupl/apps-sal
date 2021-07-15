n, l, x, y = list(map(int, input().split()))
a = set(map(int, input().split()))
ok1 = ok2 = ok3 = False
for c in a:
    if c + x in a:
        ok1 = True
    if c + y in a:
        ok2 = True
    if c - x > 0 and c - x + y in a:
        ok3 = True
        mark = c - x
    if c + x < l and c + x - y in a:
        ok3 = True
        mark = c + x
    if c + x + y in a:
        ok3 = True
        mark = c + x    
    if c - x - y in a:
        ok3 = True
        mark = c - x
if ok1 and ok2:
    print(0)
elif (not ok1) and (not ok2):    
    if ok3:
        print(1)
        print(mark)
    else:
        print(2)
        print(x, y)
else:
    print(1)
    print(y if ok1 else x)



