ch = [str(input()) for _ in range(4)]
L = [ch[0][0], ch[0][1], ch[1][1], ch[1][0]]
R = [ch[2][0], ch[2][1], ch[3][1], ch[3][0]]
del L[L.index('X')]
del R[R.index('X')]
i = 0
while i < 4 and L != R:
    i += 1
    L = L[1:] + [L[0]]
if L == R:
    print('YES')
else:
    print('NO')
