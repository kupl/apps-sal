import sys
input = sys.stdin.readline
for _ in range(int(input())):
    (a, b, c, n) = map(int, input().split())
    (a, b, c) = sorted([a, b, c])
    n -= c - a
    n -= c - b
    if n >= 0 and n % 3 == 0:
        print('YES')
    else:
        print('NO')
