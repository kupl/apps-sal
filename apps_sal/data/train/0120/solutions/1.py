import sys

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    s = (n - m) // (m + 1)
    none = (m + 1 - (n - m) % (m + 1)) * s * (s + 1) // 2 + ((n - m) % (m + 1)) * (s + 1) * (s + 2) // 2
    print((n + 1) * n // 2 - none)
