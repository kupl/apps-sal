import sys
input = sys.stdin.readline

a, b, c = list(map(int, input().split()))

aw = a // 3
bw = b // 2
cw = c // 2

MIN = min(aw, bw, cw)

ANS = MIN * 7

a -= MIN * 3
b -= MIN * 2
c -= MIN * 2
SCOREMAX = 0

for start in range(7):
    ax = a
    bx = b
    cx = c
    SCORE = 0
    R = [0, 1, 2, 0, 2, 1, 0][start:] + [0, 1, 2, 0, 2, 1, 0][:start]

    for k in R * 100:
        if k == 0:
            if ax == 0:
                break
            else:
                ax -= 1
        if k == 1:
            if bx == 0:
                break
            else:
                bx -= 1

        if k == 2:
            if cx == 0:
                break
            else:
                cx -= 1

        SCORE += 1

    SCOREMAX = max(SCOREMAX, SCORE)

print(ANS + SCOREMAX)
