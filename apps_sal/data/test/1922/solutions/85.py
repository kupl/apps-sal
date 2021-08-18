import sys
readline = sys.stdin.readline
read = sys.stdin.read

n, m = list(map(int, readline().split()))

if n == 1 and m == 1:
    print((1))
elif n == 1 or m == 1:
    print((max(n, m) - 2))
else:
    print(((n - 2) * (m - 2)))
