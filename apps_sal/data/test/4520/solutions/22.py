
import sys
import bisect

line_count = 0
segments = [None]
num_points = 200000
for line in sys.stdin.readlines():
    inputs = line.split()
    if line_count == 0:
        n = int(inputs[0])
        k = int(inputs[1])
        opening = {}
        closing = {}
        removed_right = {}
        segment_index = 0
        for i in range(1, num_points + 1):
            opening[i] = []
            closing[i] = []
            removed_right[i] = 0
    else:
        l = int(inputs[0])
        r = int(inputs[1])
        segment_index += 1
        segments.append((l, r))
        opening[l].append(segment_index)
        closing[r].append(segment_index)
    if line_count == n:
        break
    line_count += 1

working = []
removed = []
for i in range(1, num_points + 1):
    for segment_index in opening[i]:
        _, r = segments[segment_index]
        bisect.insort_right(working, (r, segment_index))
    working_count = len(working)
    while working_count > k:
        r, segment_index = working.pop()
        working_count -= 1
        removed.append(segment_index)
        removed_right[r] += 1
    squeezed_out = len(closing[i]) - removed_right[i]
    working = working[squeezed_out:]

print(len(removed))
for j in removed:
    print(j, end=" ")
