import sys
import operator as op


next(sys.stdin)

xs = list(map(int, next(sys.stdin).rstrip().split()))

if len(xs) <= 2:
    print(0)
    return

frontier = []
frontier.append((0, xs[1] - xs[0], xs[1]))
frontier.append((1, xs[1] + 1 - xs[0], xs[1] + 1))
if xs[1] > 0:
    frontier.append((1, xs[1] - 1 - xs[0], xs[1] - 1))
if xs[0] > 0:
    frontier.append((1, xs[1] - xs[0] + 1, xs[1]))
frontier.append((1, xs[1] - xs[0] - 1, xs[1]))
if xs[0] > 0:
    frontier.append((2, xs[1] + 1 - xs[0] + 1, xs[1] + 1))
frontier.append((2, xs[1] + 1 - xs[0] - 1, xs[1] + 1))
if xs[0] > 0 and xs[1] > 0:
    frontier.append((2, xs[1] - 1 - xs[0] + 1, xs[1] - 1))
if xs[1] > 0:
    frontier.append((2, xs[1] - 1 - xs[0] - 1, xs[1] - 1))


for x in xs[2:]:

    new_frontier = []

    for current, diff, last_x in frontier:

        if diff == x - last_x:
            new_frontier.append((current, diff, x))
        elif diff == x + 1 - last_x:
            new_frontier.append((current + 1, diff, x + 1))
        elif x > 0 and (diff == x - 1 - last_x):
            new_frontier.append((current + 1, diff, x - 1))

    frontier = new_frontier
    if not frontier:
        print(-1)
        return

print(min(frontier, key=op.itemgetter(0))[0])

