(a, b, c) = list(map(int, input().split()))
(x, y, z) = list(map(int, input().split()))
dx = [a - x, b - y, c - z]
splus = 0
sminus = 0
for i in dx:
    if i > 0:
        splus += i // 2
    else:
        sminus += -i
if sminus == 0 or splus >= sminus:
    print('Yes')
else:
    print('No')
