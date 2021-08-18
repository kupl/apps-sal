import sys
t = int(sys.stdin.readline())
for i in range(t):
    a = list(map(int, sys.stdin.readline().strip().split()))
    op = sum(a)
    print(op // 2)
