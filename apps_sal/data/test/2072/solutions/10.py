f = int(input())
coords = list(map(int, input().split()))
speeds = list(map(int, input().split()))
lo = min(coords)
hi = max(coords)


def calcTime(mid, speeds, coords):
    return max([abs(mid - x) / speeds[i] for (i, x) in enumerate(coords)])


minSoFar = 10 ** 12
count = 0
(ts, te) = (calcTime(lo, speeds, coords), calcTime(hi, speeds, coords))
while count < 80:
    count += 1
    mid = lo + (hi - lo) / 2
    mp = calcTime(mid, speeds, coords)
    mid2 = mid + (hi - mid) / 2
    mp2 = calcTime(mid2, speeds, coords)
    if mp2 < mp:
        lo = mid
    else:
        hi = mid2
    minSoFar = min(minSoFar, mp, mp2)
print('{0:.9f}'.format(minSoFar))
