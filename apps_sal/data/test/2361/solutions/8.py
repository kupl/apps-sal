import sys

input = sys.stdin.readline
flush = sys.stdout.flush

for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))
    if m >= n // k:
        a = n // k
        m -= a
        b = m // (k - 1) + 1 - (m % (k - 1) == 0)
        print(a - b)
        continue
    else:
        print(m)

