import sys
import bisect
next(sys.stdin)
ais = list(map(int, next(sys.stdin).rstrip().split()))
rooms = list(map(int, next(sys.stdin).rstrip().split()))
borders = [ais[0]]
for a in ais[1:]:
    borders.append(borders[-1] + a)
result = []
for room in rooms:
    dorm_num = bisect.bisect_left(borders, room) + 1
    if dorm_num > 1:
        room -= borders[dorm_num - 2]
    result.append('%s %s' % (dorm_num, room))
for r in result:
    print(r)
