days = int(input())
events = [int(_) for _ in input().split()]

rests = 0
last = 0
for event in events:
    if event == 0:
        rests += 1
        last = 0
    elif event == 1:
        if last == 1:
            rests += 1
            last = 0
        else:
            last = 1
    elif event == 2:
        if last == 2:
            rests += 1
            last = 0
        else:
            last = 2
    else:
        if last == 1:
            last = 2
        elif last == 2:
            last = 1
print(rests)
