
import sys

line_count = 0
segments = []
for line in sys.stdin.readlines():
    inputs = line.split()
    if line_count == 0:
        n = int(inputs[0])
        k = int(inputs[1])
    else:
        l = int(inputs[0])
        r = int(inputs[1])
        segments.append((l, r))
    if line_count == n:
        break
    line_count += 1

removed = [False for i in range(n)]
remove_count = 0
removed_list = []
for i in range(1, 201):
    max_i = 0
    covering = []
    for j in range(n):
        if removed[j]:
            continue
        l, r = segments[j]
        if l <= i and i <= r:
            covering.append((r, j))
    to_remove = len(covering) - k
    if to_remove > 0:
        covering.sort()
        for _ in range(to_remove):
            _, j = covering.pop()
            removed[j] = True
            removed_list.append(j)

print(len(removed_list))
for j in removed_list:
    print(j + 1, end=" ")
