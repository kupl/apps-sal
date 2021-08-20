from heapq import heappush, heappop
(bowels, Time) = map(int, input().split())
myLine = [-int(b) for b in input().split()]
gulp = []
eat = 0
for i in range(1, min(bowels + 1, Time)):
    if i >= Time:
        break
    while gulp and -gulp[0] >= Time - i:
        heappop(gulp)
    if -myLine[i - 1] < Time:
        heappush(gulp, myLine[i - 1] + i)
    eat = max(len(gulp), eat)
print(eat)
