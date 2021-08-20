import sys


def inp():
    return sys.stdin.readline().strip()


for _ in range(int(inp())):
    (a, b) = map(int, inp().split())
    print(min(a, b, (a + b) // 3))
