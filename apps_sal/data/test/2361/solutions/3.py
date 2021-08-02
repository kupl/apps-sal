import sys
input = sys.stdin.readline
for f in range(int(input())):
    n, m, k = map(int, input().split())
    c = n // k
    if m <= c:
        print(m)
    else:
        print(c - (m - c + k - 2) // (k - 1))
