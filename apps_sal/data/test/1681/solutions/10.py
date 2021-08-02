a = input()
b = input()
s = 0
ok = True
for i in range(27):
    c = chr(ord('a') + i)
    aa = a.count(c)
    bb = b.count(c)
    m = min(a.count(c), b.count(c))
    if aa == 0 and bb != 0:
        ok = False
    s = s + m
if not ok:
    print(-1)
else:
    print(s)
