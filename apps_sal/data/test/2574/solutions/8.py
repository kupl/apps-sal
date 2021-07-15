import sys

T = int(sys.stdin.readline().strip())
for t in range (0, T):
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    a.sort()
    print(max([a[0] * a[1] * a[2] * a[3] * a[-1], 
        a[0] * a[1] * a[-3] * a[-2] * a[-1], 
        a[-5] * a[-4] * a[-3] * a[-2] * a[-1]]))
