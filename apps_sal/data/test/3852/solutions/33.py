import sys


def input():
    return sys.stdin.readline().strip()


def mapint():
    return map(int, input().split())


sys.setrecursionlimit(10 ** 9)
N = int(input())
As = list(mapint())
command = []
plus_max = max(As)
minus_min = min(As)
if abs(plus_max) >= abs(minus_min):
    maxi_idx = As.index(plus_max)
    for i in range(N):
        a = As[i]
        if a < 0:
            As[i] += plus_max
            command.append((i, maxi_idx))
    for i in range(N - 1):
        a = As[i]
        b = As[i + 1]
        if a >= 0 and a > b:
            command.append((i + 1, i))
            As[i + 1] += As[i]
else:
    mini_idx = As.index(minus_min)
    for i in range(N):
        a = As[i]
        if a > 0:
            As[i] += minus_min
            command.append((i, mini_idx))
    for i in range(N - 1, 0, -1):
        a = As[i]
        b = As[i - 1]
        if a < 0 and b > a:
            command.append((i - 1, i))
            As[i - 1] += As[i]
print(len(command))
for (x, y) in command:
    print(y + 1, x + 1)
