import sys

f = sys.stdin
# f = open("input.txt", "r")

k, a, b, v = map(int, f.readline().split())

cnt = 0
boxes = 0

while cnt < a:
    if k - 1 <= b:
        cnt += k * v
        b -= k - 1
    elif b > 0:
        cnt += (b + 1) * v
        b = 0
    else:
        cnt += v
    boxes += 1

print(boxes)
