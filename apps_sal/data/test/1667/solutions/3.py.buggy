BigNum = 10 ** 10

n = int(input())
aa = [BigNum] + list(map(int, input().split(' '))) + [BigNum]
appear = sorted([(v, i) for i, v in enumerate(aa)])

ans = -1
maxLocations = 0

intervals = [(i, i) for i in range(len(aa))]
lengths = {}


def incCount(val):
    nonlocal lengths
    lengths[val] = lengths.get(val, 0) + 1


def decCount(val):
    nonlocal lengths
    if lengths[val] == 1:
        del lengths[val]
    else:
        lengths[val] -= 1


def mergeIntervals(a, b):
    return (min(a[0], b[0]), max(a[1], b[1]))


for v, i in appear:
    if v == BigNum:
        continue

    inter = intervals[i]
    if aa[i - 1] < aa[i]:
        li = intervals[i - 1]
        decCount(li[1] - li[0] + 1)
        inter = mergeIntervals(li, inter)
    if aa[i] > aa[i + 1]:
        ri = intervals[i + 1]
        decCount(ri[1] - ri[0] + 1)
        inter = mergeIntervals(ri, inter)

    intervals[inter[0]] = inter
    intervals[inter[1]] = inter
    incCount(inter[1] - inter[0] + 1)

    if len(lengths) == 1:
        count = list(lengths.values())[0]
        if count > maxLocations:
            maxLocations = count
            ans = v + 1
        #print(v + 1, count)

print(ans)
