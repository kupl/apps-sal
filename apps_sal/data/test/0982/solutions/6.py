import math
t = int(input())
for _ in range(t):
    (l, r) = map(int, input().split())
    if l * 2 > r:
        print('YES')
    else:
        print('NO')
