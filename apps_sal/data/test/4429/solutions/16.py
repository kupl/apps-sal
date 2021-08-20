import sys
input = sys.stdin.readline
for f in range(int(input())):
    (x, y, z) = map(int, input().split())
    a = min(x, y)
    b = min(x, z)
    c = min(y, z)
    if max(a, b) != x or max(a, c) != y or max(b, c) != z:
        print('NO')
    else:
        print('YES')
        print(a, b, c)
