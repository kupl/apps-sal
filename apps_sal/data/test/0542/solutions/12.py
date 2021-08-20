__author__ = 'Rakshak.R.Hegde'
n = int(input())
(w1, w2) = ([], [])
while n:
    n -= 1
    pnts = int(input())
    if pnts > 0:
        w1.append(pnts)
    else:
        w2.append(-pnts)
(sw1, sw2) = (sum(w1), sum(w2))
if sw1 == sw2:
    if w1 == w2:
        first = pnts > 0
    else:
        first = w1 > w2
else:
    first = sw1 > sw2
print('first' if first else 'second')
