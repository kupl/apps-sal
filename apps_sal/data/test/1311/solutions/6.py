import sys

n = int(input())
ranges = []
for xw in sys.stdin:
    x, w = map(int, xw.split())
    ranges.append((x + w, x - w))
ranges.sort()
result = 0
end = - float('inf')
for e, b in ranges:
    if b >= end:
        result += 1
        end = e
print(result)
