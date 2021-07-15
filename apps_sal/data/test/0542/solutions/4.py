__author__ = 'Rakshak.R.Hegde'
n = int(input())
w1, w2 = [], []
w1pnts, w2pnts = 0, 0
lastByW1 = True
while n:
    n -= 1
    pnts = int(input())
    if (pnts > 0):
        w1.append(pnts)
        w1pnts += pnts
        lastByW1 = True
    else:
        w2.append(-pnts)
        w2pnts -= pnts
        lastByW1 = False
if w1pnts == w2pnts:
    if w1 == w2:
        print('first' if lastByW1 else 'second')
    else:
        print('first' if w1 > w2 else 'second')
else:
    print('first' if w1pnts > w2pnts else 'second')
