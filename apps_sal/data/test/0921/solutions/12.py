import math
(n, w) = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
qw = l[:]
l.sort(reverse=True)
q = [int(math.ceil(x / 2)) for x in l]
sm = sum(q)
if w < sm:
    print(-1)
else:
    rem = w - sm
    er = q[:]
    for x in range(len(q)):
        if rem + q[x] > l[x]:
            rem = rem - (l[x] - q[x])
            q[x] = l[x]
        else:
            e = []
            q[x] = q[x] + rem
            for qq in qw:
                inx = l.index(qq)
                e.append(q[inx])
                print(e[-1], end=' ')
                l[inx] = -111
