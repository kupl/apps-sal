from math import sqrt

T = int(input())
for _ in range(T):
    n, d = list(map(int, input().split()))
    x = max(int(sqrt(d)) - 1, 0)
    if x + (d+x) // (x+1) <= n:
        print('YES')
    else:
        print('NO')

