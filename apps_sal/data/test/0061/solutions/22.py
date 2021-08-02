n, b = [int(i) for i in input().split(" ")]
bx = [int(i) for i in input().split(" ")]
m, a = [int(i) for i in input().split(" ")]
ax = [int(i) for i in input().split(" ")]
bb, aa = 0, 0
for i in bx:
    aa = aa * b + i
for i in ax:
    bb = bb * a + i
if aa < bb:
    print('<')
elif aa == bb:
    print('=')
else:
    print('>')
