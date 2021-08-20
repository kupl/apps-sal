q = int(input())
for rwerew in range(q):
    (a, b, c, d) = map(int, input().split())
    (x, y, x1, y1, x2, y2) = map(int, input().split())
    if x1 == x2 and (a > 0 or b > 0):
        print('No')
    elif y1 == y2 and (c > 0 or d > 0):
        print('No')
    elif x2 - x >= b - a and y2 - y >= d - c and (x - x1 >= a - b) and (y - y1 >= c - d):
        print('Yes')
    else:
        print('No')
