import sys
q = int(sys.stdin.readline())
Q = [sys.stdin.readline().split() for i in range(q)]
Lcount = 0
Rcount = 0
BOOK = [None] * (2 * 10 ** 5 + 1)
for i in range(q):
    if Q[i][0] == 'L':
        Lcount += 1
        BOOK[int(Q[i][1])] = ('L', Lcount, Rcount)
    elif Q[i][0] == 'R':
        Rcount += 1
        BOOK[int(Q[i][1])] = ('R', Lcount, Rcount)
    else:
        l = BOOK[int(Q[i][1])][1]
        r = BOOK[int(Q[i][1])][2]
        if BOOK[int(Q[i][1])][0] == 'R':
            ANS = min(Rcount - r, Lcount - l + (r + l - 1))
        elif BOOK[int(Q[i][1])][0] == 'L':
            ANS = min(Lcount - l, Rcount - r + (r + l - 1))
        sys.stdout.write(str(ANS) + '\n')
