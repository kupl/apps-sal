g = [-1, 0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
(x, y) = map(int, input().split())
if g[x] == g[y]:
    print('Yes')
else:
    print('No')
