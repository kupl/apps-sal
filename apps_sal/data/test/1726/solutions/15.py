(days, read) = map(int, input().split(' '))
day = 0
schedule = [int(x) for x in input().strip().split(' ')]
for s in schedule:
    toread = 86400 - s
    read -= toread
    day += 1
    if read <= 0:
        break
print(day)
