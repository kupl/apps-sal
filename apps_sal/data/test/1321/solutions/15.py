import sys

n = int(sys.stdin.readline())
width = {}
heights = []
for i in range(n):
    w, h = list(map(int, sys.stdin.readline().strip().split()))
    heights.append((h, i))
    width[i] = w
total_width = sum(width.values())

heights.sort(reverse=True)
for i in range(n):
    w = total_width - width[i]
    h = heights[0][0] if heights[0][1] != i else heights[1][0]
    sys.stdout.write(str(w * h) + ' ')
