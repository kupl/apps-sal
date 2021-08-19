"""input
329 19913 19900
"""


def win(s):
    i = s // 50 % 475
    l = []
    for _ in range(25):
        i = (i * 96 + 42) % 475
        l.append(26 + i)
    return l


(p, x, y) = list(map(int, input().split()))
(c, x1) = (0, x)
while x - 50 >= y:
    x -= 50
while p not in win(x):
    x += 50
    if x > x1:
        c += 50
print(c // 100 if c % 100 == 0 else c // 100 + 1)
