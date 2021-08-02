s = input()
a = s.split()

tot = 0
b = [1 if x == '?' else x for x in a]
for i, x in enumerate(b):
    if x == 1:
        if i == 0 or b[i - 1] == '+':
            tot += 1
        elif b[i - 1] == '-':
            tot -= 1

goal = int(b[-1])
if tot < goal:
    for i, x in enumerate(b):
        if x == 1 and i == 0 or b[i - 1] == '+' and tot < goal:
            a = min(goal - 1, goal - tot)
            tot += a
            b[i] += a

elif tot > goal:
    for i, x in enumerate(b):
        if x == 1 and b[i - 1] == '-' and tot > goal:
            a = min(goal - 1, tot - goal)
            tot -= a
            b[i] += a

if tot != goal:
    print("Impossible")
else:
    print("Possible")
    print(' '.join([str(x) for x in b]))
