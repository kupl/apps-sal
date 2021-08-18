import math
import sys
import time

length = int(input())
heights = [int(x) for x in input().split(' ')]
start = time.time()
cache = {}
cache[(length, heights[length - 1])] = []
cache[(length, heights[length - 2] - 1)] = []


def min_list(modifyable, modifier):
    for i in range(0, len(modifier)):
        if (i == len(modifyable)):
            modifyable.append(modifier[i])
        else:
            modifyable[i] = min(modifyable[i], modifier[i])


def new_step(index, last_height):
    height = heights[index]
    if index == length - 1:
        return [max(0, last_height - height + 1)]

    next_height = heights[index + 1]

    result = cache[(index + 1, height)].copy()
    b = cache[(index + 2, next_height)]
    min_list(result, b)

    new_difference = max(0, last_height - height + 1) + max(0, next_height - height + 1)
    c = [new_difference]
    d = cache[(index + 2, min(next_height, height - 1))]
    for value in d:
        c.append(value + new_difference)
    min_list(result, c)
    return result


i = length - 1
while i > 0:
    cache[(i, heights[i - 1])] = new_step(i, heights[i - 1])

    if i > 1 and heights[i - 2] <= heights[i - 1]:
        cache[(i, heights[i - 2] - 1)] = new_step(i, heights[i - 2] - 1)

    i -= 1

print(' '.join(map(str, new_step(0, -sys.maxsize))))
end = time.time()
