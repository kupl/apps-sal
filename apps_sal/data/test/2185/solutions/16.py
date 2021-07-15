import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    f = []
    p = None
    for d in (x - y for x, y in zip(a, b)):
        if d != p and (d != 0 or f):
            f.append(d)
        p = d
    while f and f[-1] == 0:
        f.pop()
    print('YES' if not f or len(f) == 1 and f[0] < 0 else 'NO')
