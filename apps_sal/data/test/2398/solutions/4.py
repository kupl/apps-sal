import sys
input = sys.stdin.readline

for _ in range(int(input())):
    left, right, up, down = list(map(int, input().split()))
    x, y, x1, y1, x2, y2 = list(map(int, input().split()))

    if (left or right) and (x1 == x2) or (up or down) and (y1 == y2):
        print('No')
        continue
    if (x1 <= x + (right - left) <= x2) and (y1 <= y + (down - up) <= y2):
        print('Yes')
    else:
        print('No')
