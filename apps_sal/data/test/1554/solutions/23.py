pearl_count = int(input())
pearls = [int(pearl) for pearl in input().split()]
recorded = set()
intervals = []
begin = 1
for i in range(pearl_count):
    if pearls[i] in recorded:
        intervals.append([begin, i + 1])
        recorded = set()
        begin = i + 2
    else:
        recorded.add(pearls[i])
if intervals:
   intervals[-1][-1] = pearl_count
   print(len(intervals))
   [print(' '.join(map(str, interval))) for interval in intervals]
else:
    print(-1)
