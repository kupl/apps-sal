import sys

values = [int(x) for x in sys.stdin.readline().split()]
n_glasses, start, end = values[0], values[1], values[2]
positions = [int(x) for x in sys.stdin.readline().split()]
used = {}
min_swaps = 0

start -= 1

while start != end - 1:
    if start in used:
        print("-1")
        return
    min_swaps += 1
    used[start] = True
    start = positions[start] - 1

print(min_swaps)
