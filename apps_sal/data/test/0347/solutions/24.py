__author__ = 'MoonBall'
import sys
T = 1


def process():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    z = [500, 1000, 1500, 2000, 2500]
    total = 0
    for _ in range(5):
        total += max(0.3 * z[_], (1 - a[_] / 250) * z[_] - 50 * b[_])
    total += 100 * c[0] - 50 * c[1]
    print(int(total))


for _ in range(T):
    process()
