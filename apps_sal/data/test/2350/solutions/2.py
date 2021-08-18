import sys


def pprint(s): return print(' '.join(map(str, s)))
def input(): return sys.stdin.readline().strip()


ipnut = input
for i in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    print(1 + (x1 - x2) * (y1 - y2))
