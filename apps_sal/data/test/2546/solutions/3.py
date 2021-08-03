import sys


def I():
    return sys.stdin.readline().rstrip()


for _ in range(int(I())):
    n, s = list(map(int, I().split()))
    half = n // 2
    lows = 0
    l, r = [], []
    for _ in range(n):
        x, y = list(map(int, I().split()))
        lows += x
        l.append(x)
        r.append(y)
    money = 0
    t = 1
    while t <= 1e9:
        t *= 2
    t //= 2
    while t > 0:
        people = 0
        new_money = money + t
        left = []
        for low, high in zip(l, r):
            if low <= new_money <= high:
                left.append(new_money - low)
            elif new_money < low:
                people += 1
        left.sort()
        people = half + 1 - people
        if people <= 0 or len(left) >= people and lows + sum(left[:people]) <= s:
            money += t
        t //= 2
    print(money)
