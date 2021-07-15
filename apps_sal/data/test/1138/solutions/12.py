R, L, U, D = 0, 0, 0, 0

for c in input():
    if c == 'R':
        R += 1
    elif c == 'L':
        L += 1
    elif c == 'U':
        U += 1
    elif c == 'D':
        D += 1

diff_RL = abs(R-L)
diff_UD = abs(U-D)

if (diff_RL % 2 == 0 and diff_UD % 2 == 0) or (diff_RL % 2 == 1 and diff_UD % 2 == 1):
    print((diff_RL+diff_UD) // 2)
else:
    print(-1)
