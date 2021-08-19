from sys import stdin
__author__ = 'artyom'


def read_next_line():
    return list(map(int, stdin.readline().strip().split()))


(x, y, m) = read_next_line()
a = [x, y]
x = min(a)
y = max(a)
if y <= 0 and m > y:
    print(-1)
else:
    count = 0
    if x < 0 and m > y:
        count = -(x // y)
        x = x % y
    while m > y:
        tmp = y
        y = x + y
        x = tmp
        count += 1
    print(count)
