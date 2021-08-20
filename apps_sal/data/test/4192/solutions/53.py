(distance, time, speed) = map(int, input().split())
if distance / speed <= time:
    print('Yes')
else:
    print('No')
