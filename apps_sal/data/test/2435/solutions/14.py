import sys
input = sys.stdin.readline
t = int(input())
for tests in range(t):
    (n, x, m) = list(map(int, input().split()))
    LR = [tuple(map(int, input().split())) for i in range(m)]
    R = x
    L = x
    for (l, r) in LR:
        if l <= R <= r:
            R = r
        if l <= L <= r:
            L = l
    print(1 + R - L)
