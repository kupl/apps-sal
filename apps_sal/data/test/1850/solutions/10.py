import bisect
(n, d) = list(map(int, input().strip().split()))
d = d - 1
curscore = list(map(int, input().strip().split()))
nextp = list(map(int, input().strip().split()))
lenarr = len(curscore)
newscore = curscore[d] + nextp.pop(0)
nextp.sort()
curscore.sort()
indexmax = bisect.bisect(curscore, newscore)
indexmin = bisect.bisect(curscore, curscore[lenarr - 1 - d])
largerpoint = 0
for i in range(indexmin, indexmax):
    subval = newscore - curscore[i]
    indexsub = bisect.bisect(nextp, subval) - 1
    if indexsub < 0:
        largerpoint += 1
        continue
    else:
        nextp.pop(indexsub)
print(len(curscore) - indexmax + largerpoint + 1)
