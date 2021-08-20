(n, c) = [int(x) for x in input().split(' ')]
P = [int(x) for x in input().split(' ')]
T = [int(x) for x in input().split(' ')]


def score(P, T, c):
    s = 0
    x = 0
    for (p, t) in zip(P, T):
        x += t
        s += max(0, p - c * x)
    return s


Limak = score(P, T, c)
Radewoosh = score(reversed(P), reversed(T), c)
if Limak > Radewoosh:
    print('Limak')
elif Limak < Radewoosh:
    print('Radewoosh')
else:
    print('Tie')
