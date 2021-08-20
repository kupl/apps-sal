import datetime
n = int(input())
dts_i = [[int(y) for y in input().split(':')] for x in range(n)]
dts = []
for (h, m) in dts_i:
    dts.append(datetime.datetime(2017, 1, 1, h, m))
for (h, m) in dts_i:
    dts.append(datetime.datetime(2017, 1, 2, h, m))
for (h, m) in dts_i:
    dts.append(datetime.datetime(2017, 1, 3, h, m))
dts = sorted(dts)
pairs = list(zip(dts, dts[1:]))
(lo, hi) = max(pairs, key=lambda xy: xy[1] - xy[0])
delta = hi - lo - datetime.timedelta(minutes=1)
(hours, remainder) = divmod(delta.seconds, 3600)
(minutes, seconds) = divmod(remainder, 60)
print('{0:02d}:{1:02d}'.format(hours, minutes))
