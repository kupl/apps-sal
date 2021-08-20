(n, m, x, y) = map(int, input().split())
xl = list(map(int, input().split()))
yl = list(map(int, input().split()))
if max(xl) < min(yl) and x < min(yl) and (max(xl) < y):
    print('No War')
else:
    print('War')
