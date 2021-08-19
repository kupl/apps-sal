(n, m) = map(int, input().split())
P = []
Y = []
I = []
for i in range(m):
    (a, b) = map(int, input().split())
    P.append(a)
    Y.append(b)
    I.append(i)
Z = zip(P, Y, I)
Z = sorted(Z)
(P, Y, I) = zip(*Z)
N = []
c = P[0]
d = 1
for i in range(m):
    if c == P[i]:
        N.append('{0:06d}{1:06d}'.format(c, d))
        d += 1
    else:
        c = P[i]
        d = 1
        N.append('{0:06d}{1:06d}'.format(c, d))
        d += 1
Z = zip(I, N)
Z = sorted(Z)
(I, N) = zip(*Z)
for i in N:
    print(i)
