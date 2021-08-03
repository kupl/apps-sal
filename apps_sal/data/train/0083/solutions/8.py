import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for x, y, a, b in Query:
    d = y - x
    r = a + b
    if d % r == 0:
        print(d // r)
    else:
        print(-1)
