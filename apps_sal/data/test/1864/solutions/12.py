import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
if 1 not in a:
    print(1)
else:
    print(-1)
