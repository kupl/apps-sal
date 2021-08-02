from sys import stdin

n, t = [int(x) for x in stdin.readline().strip().split()]
queue = [x for x in stdin.readline().strip()]
i, changes = 0, True

while changes and i < t:
    changes, j = False, 1
    while j < n:
        if queue[j - 1] == 'B' and queue[j] == 'G':
            queue[j - 1], queue[j], changes, j = 'G', 'B', True, j + 1
        j += 1
    i += 1
print(''.join(queue))
