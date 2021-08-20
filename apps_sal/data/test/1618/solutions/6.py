import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
x = 0
for i in range(m):
    (w, h) = map(int, sys.stdin.readline().split())
    x = max(x, l[w - 1])
    sys.stdout.write(str(x) + '\n')
    x += h
