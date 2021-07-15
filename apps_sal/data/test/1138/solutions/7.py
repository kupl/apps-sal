a = input()
L, R, U, D = 0, 0, 0, 0
for i in a:
    if i == 'L':
        L += 1
    elif i == 'R':
        R += 1
    elif i == 'U':
        U += 1
    elif i == 'D':
        D += 1
UD = abs(U - D)
LR = abs(L - R)
if len(a) % 2 != 0:
    print("-1")
elif UD == 0 and LR == 0:
    print('0')
else:
    x = UD + LR
    if x % 2 != 0:
        print("-1")
    else:
        print(x // 2)
