cups = [int(i) for i in input().split(' ')]
medals = [int(i) for i in input().split(' ')]
shelves = int(input())
sCups = sum(cups)
sMedals = sum(medals)
k = 0
l = 0
if sCups % 5 != 0:
    k = 1
if sMedals % 10 != 0:
    l = 1
minShelvesRequired = int(sCups / 5) + k + int(sMedals / 10) + l
if minShelvesRequired <= shelves:
    print('YES')
else:
    print('NO')
