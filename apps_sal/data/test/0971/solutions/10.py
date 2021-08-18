nbd = list(map(int, input().split()))
oranges = list(map(int, input().split()))
numTimesEmptied = 0
total = 0
for orange in oranges:
    if orange <= nbd[1]:
        total += orange
        if total > nbd[2]:
            numTimesEmptied += 1
            total = 0
print(numTimesEmptied)
