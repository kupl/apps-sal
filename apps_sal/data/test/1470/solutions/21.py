import sys

x = int(sys.stdin.readline())
n = x // 11
r = x % 11
if r == 0:
    print(2*n)
elif r <= 6:
    print(2*n + 1)
else:
    print(2 * (n+1))
