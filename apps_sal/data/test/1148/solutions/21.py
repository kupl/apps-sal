import sys

n = int(input())
paint = list(map(int, input().split()))
low, high = min(paint), max(paint)
if low == high:
    print(n * low)
    return

count, best = 0, 0
start = paint.index(low)
pos = start
while True:
    pos += 1
    if pos == n:
        pos = 0
    if pos == start:
        break
    if paint[pos] != low:
        count += 1
        best = max(best, count)
    else:
        count = 0
print(n * low + best)

