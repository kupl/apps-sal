import sys
t = 1
t = int(input())
for i in range(t):
    x, y, n = list(map(int, sys.stdin.readline().strip().split()))

    a = (n // x) * x + y
    b = ((n // x) - 1) * x + y

    if(a <= n):
        print(a)
    else:
        print(b)
