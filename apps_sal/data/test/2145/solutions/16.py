import sys


def I():
    return sys.stdin.readline().rstrip()


for _ in range(int(I())):
    (x, y) = list(map(int, I().split()))
    print('YES' if x > 3 or (x == 1 and y == 1) or (2 <= x <= 3 and 1 <= y <= 3) else 'NO')
