from bisect import *

n, m, k, q = list(map(int, input().split()))
right = [-1] * n
left = [-1] * n
for i in range(k):
    row, col = list(map(int, input().split()))
    row -= 1
    col -= 1
    if right[row] == -1:
        right[row] = left[row] = col
    else:
        right[row] = max(right[row], col)
        left[row] = min(left[row], col)
safe = sorted(list([int(qi) - 1 for qi in input().split()]))


# print(safe)

def dist(lower, upper, row):
    if lower > upper:
        return dist(upper, lower, row)
    pos = bisect_left(safe, lower)
    options = []
    if pos < len(safe):
        if safe[pos] <= upper:
            return upper - lower
        else:
            options.append(safe[pos] - lower + safe[pos] - upper)
    pos2 = bisect_left(safe, lower) - 1
    if pos2 >= 0:
        options.append(lower - safe[pos2] + upper - safe[pos2])
    return min(options)


if left[0] == -1:
    left[0] = right[0] = 0
dleft = right[0] + (right[0] - left[0])
dright = right[0]
lastn = 0
for i in range(1, n):
    if left[i] == -1:
        continue
    ilen = right[i] - left[i]
    dleft_new = min(dleft + dist(left[lastn], right[i], i), dright + dist(right[lastn], right[i], i)) + ilen
    dright_new = min(dleft + dist(left[lastn], left[i], i), dright + dist(right[lastn], left[i], i)) + ilen
    dleft, dright = dleft_new, dright_new
    lastn = i
print(min(dleft, dright) + lastn)
