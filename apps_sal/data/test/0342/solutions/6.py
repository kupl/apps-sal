import sys
input = sys.stdin.readline


def mii():
    return list(map(int, input().split()))


(a, b, c) = mii()
d = min(a, b)
a -= d
b -= d
c += d
print(c * 2 + min(1, max(a, b)))
