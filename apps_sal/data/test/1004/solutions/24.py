n = int(input())
a = list([int(x) for x in input().split()])
c = []
s = 0
enter = [False] * 1000001
left = [False] * 1000001
today = []

for ai in a:
    if ai > 0 and (enter[ai] or left[ai]):
        c = []
        break

    if ai < 0 and (not enter[-ai] or left[-ai]):
        c = []
        break

    s += ai
    if ai > 0:
        enter[ai] = True
        today.append(ai)
    else:
        left[-ai] = True
        enter[-ai] = False
        if s == 0:
            c.append((len(today)))
            for x in today:
                enter[x] = False
                left[x] = False
            today = []


if len(c) > 0 and s == 0:
    print(str(len(c)))
    print(' '.join(str(x * 2) for x in c))
else:
    print(-1)
