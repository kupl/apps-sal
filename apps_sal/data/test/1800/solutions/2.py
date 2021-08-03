import sys

n, m = [int(x) for x in input().split()]
notes = [int(x) for x in input().split()]
managers = []
for line in sys.stdin:
    managers.append(tuple(int(x) for x in line.split()))

bearing_managers = []
M, T = 0, 0
for t, r in reversed(managers):
    if r > M:
        if t == T:
            bearing_managers[-1] = (t, r)
        else:
            T = t
            bearing_managers.append((t, r))
        M = r
bearing_managers.reverse()
t, r = bearing_managers[0]
bearing_managers.append((2 if bearing_managers[-1][0] == 1 else 1, 0))
L, R = 0, r - 1
sorted_part = list(sorted(notes[:r]))
for t1, r1 in bearing_managers:
    if t1 == 2:
        for i in range(r - 1, r1 - 1, -1):
            notes[i] = sorted_part[R]
            R -= 1
    else:
        for i in range(r - 1, r1 - 1, -1):
            notes[i] = sorted_part[L]
            L += 1
    r = r1

for x in notes:
    sys.stdout.write(str(x) + ' ')
