import sys

# inf = open('input.txt', 'r')
# reader = (line.rstrip() for line in inf)
reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__

t = int(input())
for _ in range(t):
    n = int(input())
    coms = list(input())
    pos = {(0, 0): -1}
    x = y = 0
    l = -1
    r = float('inf')
    for i, d in enumerate(coms):
        if d == 'L':
            x -= 1
        elif d == 'R':
            x += 1
        elif d == 'U':
            y += 1
        else:
            y -= 1

        if (x, y) in pos:
            prev = pos[(x, y)]
            if i - prev < r - l:
                r, l = i, prev
        pos[(x, y)] = i

    if r == float('inf'):
        print(-1)
    else:
        print(l + 2, r + 1)

# inf.close()
