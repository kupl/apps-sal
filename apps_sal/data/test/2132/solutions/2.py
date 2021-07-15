n = int(input())

events = []
for i in range(n):
    events.append(list([int(s) for s in input().split()]))

max_speeds = []
overtaking_forbidden = 0

current_speed = 0

ignores = 0

for event in events:
    if event[0] == 1:
        current_speed = event[1]

        while max_speeds and current_speed > max_speeds[-1]:
            max_speeds.pop()
            ignores += 1

    elif event[0] == 2:
        ignores += overtaking_forbidden
        overtaking_forbidden = 0

    elif event[0] == 3:
        if current_speed > event[1]:
            ignores += 1
        else:
            max_speeds.append(event[1])

    elif event[0] == 4:
        overtaking_forbidden = 0
    elif event[0] == 5:
        max_speeds = []
    elif event[0] == 6:
        overtaking_forbidden += 1

print(ignores)


