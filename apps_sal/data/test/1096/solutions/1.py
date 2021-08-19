cd = input()
c = cd[0]
d = cd[1]
ss = 0
if c == 'a' or c == 'h':
    ss += 1
if d == '1' or d == '8':
    ss += 1
if ss == 2:
    print(3)
elif ss == 1:
    print(5)
else:
    print(8)
