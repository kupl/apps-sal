from sys import stdin, stderr


def rl():
    return [int(w) for w in stdin.readline().split()]


(t,) = rl()
for _ in range(t):
    (x1, y1, x2, y2) = rl()
    dx = x2 - x1
    dy = y2 - y1
    print(dx * dy + 1)
