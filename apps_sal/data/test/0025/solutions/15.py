"""input
4 5
"""
(n, k) = list(map(int, input().split()))
m = [['0'] * n for _ in range(n)]
for x in range(n):
    for y in range(x, n):
        if x == y and k >= 1:
            m[x][y] = '1'
            k -= 1
        elif k >= 2:
            m[x][y] = '1'
            m[y][x] = '1'
            k -= 2
if k > 0:
    print(-1)
else:
    print('\n'.join([' '.join(i) for i in m]))
