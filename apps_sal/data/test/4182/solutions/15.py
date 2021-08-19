(n, m, x, y) = map(int, input().split())
xl = list(map(int, input().split()))
yl = list(map(int, input().split()))
xl.append(x)
yl.append(y)
if max(xl) < min(yl):
    print('No War')
else:
    print('War')
