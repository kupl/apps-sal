dx = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
dy = {'U': 1, 'D': -1, 'L': 0, 'R': 0}
x, y, xl, yl = 0, 0, [], []
a, b = list(map(int, input().split()))
for ch in input():
    xl.append(x)
    yl.append(y)
    x += dx[ch]
    y += dy[ch]
for xi, yi in zip(xl, yl):
    mx, my = a - xi, b - yi
    if x == 0 and mx != 0 or x != 0 and (mx % x != 0 or mx // x < 0):
        continue
    if y == 0 and my != 0 or y != 0 and (my % y != 0 or my // y < 0):
        continue
    if x != 0 and y != 0 and mx // x != my // y:
        continue
    print('Yes')
    return
print('No')
