s = input()
x, y = list(map(int, input().split()))

s2 = s.split('T')
sXs = list(map(len, s2[0::2]))
sYs = list(map(len, s2[1::2]))

memoX = [{sXs[0]}, set()]
for i, sX in enumerate(sXs[1:]):
    memoX[1 - i % 2] = set()
    for p in memoX[i % 2]:
        memoX[1 - i % 2].add(p + sX)
        memoX[1 - i % 2].add(p - sX)

memoY = [{0}, set()]
for i, sY in enumerate(sYs):
    memoY[1 - i % 2] = set()
    for p in memoY[i % 2]:
        memoY[1 - i % 2].add(p + sY)
        memoY[1 - i % 2].add(p - sY)

if x in memoX[1 - len(sXs) % 2] and y in memoY[len(sYs) % 2]:
    print('Yes')
else:
    print('No')

