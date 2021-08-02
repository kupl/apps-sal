# using the min-heap
from heapq import heappush, heappop
bowels, Time = map(int, input().split())
myLine = [-int(b) for b in input().split()]
gulp = []; eat = 0
for i in range(1, min(bowels + 1, Time)):
    # Terminate in cases where bowels > Time
    if i >= Time:
        break
    while gulp and -gulp[0] >= Time - i:
        # remove the bowel with the highest time penalty
        heappop(gulp)
    # Check if the option is viable
    if -myLine[i - 1] < Time:
        # Remove the step penalty and store the remaining
        heappush(gulp, myLine[i - 1] + i)
    eat = max(len(gulp), eat)
print(eat)
