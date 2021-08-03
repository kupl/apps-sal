import sys

T = int(sys.stdin.readline().strip())

for i in range(0, T):
    x = sys.stdin.readline().strip()
    y = sys.stdin.readline().strip()
    w = 0
    while y[-w - 1] == '0':
        w = w + 1
    v = w
    while x[-v - 1] == '0':
        v = v + 1
    print(v - w)
