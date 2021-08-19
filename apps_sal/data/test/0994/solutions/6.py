import sys


def maxheight(start, end):
    (start_day, start_height) = start
    (end_day, end_height) = end
    ddays = end_day - start_day
    dheight = end_height - start_height
    xdays = ddays - abs(dheight)
    if xdays < 0:
        return -1
    else:
        return xdays // 2 + max(start_height, end_height)


data = sys.stdin
days = int(data.readline().split()[0])
entries = []
for l in data.read().splitlines():
    entries.append(tuple(map(int, l.split(' '))))
entries.sort()
maxheights = []
for e in entries:
    maxheights.append(e[1])
for i in range(len(entries) - 1):
    h = maxheight(entries[i], entries[i + 1])
    if h < 0:
        print('IMPOSSIBLE')
        break
    else:
        maxheights.append(h)
else:
    first = entries[0]
    maxheights.append(first[0] - 1 + first[1])
    last = entries[-1]
    maxheights.append(days - last[0] + last[1])
    print(str(max(maxheights)))
