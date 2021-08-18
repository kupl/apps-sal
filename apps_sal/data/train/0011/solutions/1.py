import sys
input = sys.stdin.readline

Q = int(input())

for testcases in range(Q):
    S = input().strip()

    X = Y = 0
    MAXX = MINX = MAXY = MINY = 0

    for s in S:
        if s == "D":
            X += 1
            MAXX = max(MAXX, X)

        elif s == "A":
            X -= 1
            MINX = min(MINX, X)

        elif s == "W":
            Y += 1
            MAXY = max(MAXY, Y)

        else:
            Y -= 1
            MINY = min(MINY, Y)

    MAXXLIST = []
    MINXLIST = []
    MAXYLIST = []
    MINYLIST = []

    if MAXX == 0:
        MAXXLIST.append(0)

    if MAXY == 0:
        MAXYLIST.append(0)

    if MINX == 0:
        MINXLIST.append(0)

    if MINY == 0:
        MINYLIST.append(0)

    X = Y = 0

    for i in range(len(S)):
        s = S[i]
        if s == "D":
            X += 1
            if X == MAXX:
                MAXXLIST.append(i + 1)

        elif s == "A":
            X -= 1
            if X == MINX:
                MINXLIST.append(i + 1)

        elif s == "W":
            Y += 1
            if Y == MAXY:
                MAXYLIST.append(i + 1)

        else:
            Y -= 1
            if Y == MINY:
                MINYLIST.append(i + 1)

    ANS = (MAXX - MINX + 1) * (MAXY - MINY + 1)

    if MAXX - MINX > 1:
        if MAXXLIST[0] > MINXLIST[-1] or MINXLIST[0] > MAXXLIST[-1]:
            ANS = min(ANS, (MAXX - MINX) * (MAXY - MINY + 1))

    if MAXY - MINY > 1:
        if MAXYLIST[0] > MINYLIST[-1] or MINYLIST[0] > MAXYLIST[-1]:
            ANS = min(ANS, (MAXX - MINX + 1) * (MAXY - MINY))

    print(ANS)
