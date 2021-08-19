from sys import stdin, stderr


def rl():
    return [int(w) for w in stdin.readline().split()]


(t,) = rl()
for _ in range(t):
    (a, b, x, y) = rl()
    print(max(x * b, y * a, (a - x - 1) * b, (b - y - 1) * a))
