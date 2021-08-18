import sys


def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def input(): return sys.stdin.readline().strip()


def compute(start, end):
    if start == end:
        return 0
    t = abs(end)
    step = 0
    curr = start
    while True:
        curr += (step + 1)
        if curr >= t:
            if (curr - t) % 2 == 0:
                return step + 1
        step += 1


T = int(input())
while T:
    x, y = get_ints()
    start = min(x, y)
    end = max(x, y)
    ans = compute(start, end)
    print(ans)
    T -= 1
