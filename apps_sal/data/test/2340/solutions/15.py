'''input
1
10000 7
10000 8 7 6 5 3 2
'''
from sys import stdin
from bisect import bisect_left


q = int(stdin.readline().strip())
for _ in range(q):
    h, n = list(map(int, stdin.readline().split()))
    moved = set(list(map(int, stdin.readline().split())))
    original = list(moved)
    original.sort()
    pos = h
    count = 0
    while pos > 0:
        if pos - 1 in moved:
            if pos - 2 in moved:
                pos -= 2

            else:
                if pos - 2 != 0:
                    count += 1
                    pos -= 2
                else:
                    pos -= 2

        else:
            index = bisect_left(original, pos)
            if index == 0:
                pos = 0
            else:
                pos = original[index - 1] + 1
            moved.add(pos)
    print(count)
