import sys


def mp():
    return list(map(int, sys.stdin.readline().split()))


n = int(input())
a = sorted(list(mp()))
w = 0
i = 1
b = 0
j = 2
for x in range(n // 2):
    w += abs(a[x] - i)
    b += abs(a[x] - j)
    i += 2
    j += 2
print(min(w, b))
