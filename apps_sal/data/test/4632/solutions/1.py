import sys
input = sys.stdin.readline
t = int(input())
for test in range(t):
    n = int(input())
    P = [tuple(map(int, input().split())) for i in range(n)]
    P.sort()
    ANS = []
    NOWX = 0
    NOWY = 0
    for (x, y) in P:
        if x < NOWX or y < NOWY:
            print('NO')
            break
        ANS.extend(['R'] * (x - NOWX) + ['U'] * (y - NOWY))
        NOWX = x
        NOWY = y
    else:
        print('YES')
        print(''.join(ANS))
