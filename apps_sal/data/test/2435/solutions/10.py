import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x, m = list(map(int, input().split()))
    L = x
    R = x
    for i in range(m):
        l, r = list(map(int, input().split()))
        if R < l or r < L:
            continue
        else:
            R = max(R, r)
            L = min(l, L)
    print(R - L + 1)
