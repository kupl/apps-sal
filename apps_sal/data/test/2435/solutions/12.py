import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n, x, m = list(map(int, input().split()))
    info = [list(map(int, input().split())) for i in range(m)]
    x -= 1
    ansl, ansr = x, x + 1
    for l, r in info:
        l -= 1
        if max(l, ansl) < min(r, ansr):
            ansl = min(l, ansl)
            ansr = max(r, ansr)
    print(ansr - ansl)
